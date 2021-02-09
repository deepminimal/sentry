from sentry.tasks.base import instrumented_task
from sentry.utils.safe import safe_execute


@instrumented_task(name="sentry.tasks.user_report")
def user_report(report, project_id):
    """
    TODO MARCOS describe
    Create and send a UserReport.

    :param report:
    :param project_id:
    """
    from sentry.mail import mail_adapter
    from sentry.models import Project

    project = Project.objects.get_from_cache(id=project_id)
    safe_execute(mail_adapter.handle_user_report, report=report, project=project)
