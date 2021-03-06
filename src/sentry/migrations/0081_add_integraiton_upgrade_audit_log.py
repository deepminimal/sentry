# Generated by Django 1.11.29 on 2020-05-29 15:18

from django.db import migrations
import sentry.db.models.fields.bounded


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    atomic = True

    dependencies = [("sentry", "0080_alert_rules_drop_unused_tables_cols")]

    operations = [
        migrations.AlterField(
            model_name="auditlogentry",
            name="event",
            field=sentry.db.models.fields.bounded.BoundedPositiveIntegerField(
                choices=[
                    (1, "member.invite"),
                    (2, "member.add"),
                    (3, "member.accept-invite"),
                    (5, "member.remove"),
                    (4, "member.edit"),
                    (6, "member.join-team"),
                    (7, "member.leave-team"),
                    (8, "member.pending"),
                    (20, "team.create"),
                    (21, "team.edit"),
                    (22, "team.remove"),
                    (30, "project.create"),
                    (31, "project.edit"),
                    (32, "project.remove"),
                    (33, "project.set-public"),
                    (34, "project.set-private"),
                    (35, "project.request-transfer"),
                    (36, "project.accept-transfer"),
                    (37, "project.enable"),
                    (38, "project.disable"),
                    (10, "org.create"),
                    (11, "org.edit"),
                    (12, "org.remove"),
                    (13, "org.restore"),
                    (40, "tagkey.remove"),
                    (50, "projectkey.create"),
                    (51, "projectkey.edit"),
                    (52, "projectkey.remove"),
                    (53, "projectkey.enable"),
                    (53, "projectkey.disable"),
                    (60, "sso.enable"),
                    (61, "sso.disable"),
                    (62, "sso.edit"),
                    (63, "sso-identity.link"),
                    (70, "api-key.create"),
                    (71, "api-key.edit"),
                    (72, "api-key.remove"),
                    (80, "rule.create"),
                    (81, "rule.edit"),
                    (82, "rule.remove"),
                    (100, "servicehook.create"),
                    (101, "servicehook.edit"),
                    (102, "servicehook.remove"),
                    (103, "servicehook.enable"),
                    (104, "servicehook.disable"),
                    (109, "integration.upgrade"),
                    (110, "integration.add"),
                    (111, "integration.edit"),
                    (112, "integration.remove"),
                    (113, "sentry-app.add"),
                    (115, "sentry-app.remove"),
                    (116, "sentry-app.install"),
                    (117, "sentry-app.uninstall"),
                    (130, "internal-integration.create"),
                    (135, "internal-integration.add-token"),
                    (136, "internal-integration.remove-token"),
                    (90, "ondemand.edit"),
                    (91, "trial.started"),
                    (92, "plan.changed"),
                    (93, "plan.cancelled"),
                    (140, "invite-request.create"),
                    (141, "invite-request.remove"),
                ]
            ),
        )
    ]
