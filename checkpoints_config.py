from great_expectations.checkpoint import SimpleCheckpoint

def create_checkpoint(context, name, batch_request, suite_name):
    checkpoint = SimpleCheckpoint(
        name=name,
        data_context=context,
        validations=[{
            "batch_request": batch_request,
            "expectation_suite_name": suite_name,
        }],
    )
    result = checkpoint.run()
    return result