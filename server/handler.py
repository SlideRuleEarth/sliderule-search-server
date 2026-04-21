"""Lambda entrypoint. Mangum wraps the ASGI app for the Lambda runtime.

Also handles EventBridge scheduled-invoke warmup events — see the
branch in lambda_handler and terraform/modules/warmer.tf for the
design rationale.
"""

from mangum import Mangum

from server.app import app, CORPORA

_mangum_handler = Mangum(app, lifespan="off")


def lambda_handler(event, context):
    # EventBridge warmup: short-circuit before Mangum. A scheduled-rule
    # invocation's only job is to count as "recent activity" so AWS
    # doesn't reap the container; reaching this function body at all
    # means CORPORA + MODEL are already loaded (they're module-level
    # globals populated at cold start), which is the whole point.
    #
    # Mangum can't parse EventBridge events — they're not HTTP-shaped —
    # so we have to branch before handing off. Detection keys off the
    # canonical envelope fields EventBridge always emits. Return value
    # is ignored by EventBridge but surfaces in CloudWatch logs as a
    # grep-able confirmation.
    #
    # See terraform/modules/warmer.tf for the rule that drives this.
    if event.get("source") == "aws.events" and event.get("detail-type") == "Scheduled Event":
        return {"warmup": "ok", "corpora": list(CORPORA.keys())}
    return _mangum_handler(event, context)
