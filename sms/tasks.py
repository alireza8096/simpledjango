from celery import shared_task


@shared_task
def temp():
    print('done')
    # Another trick
    return 'done!'