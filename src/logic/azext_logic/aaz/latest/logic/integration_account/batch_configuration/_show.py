# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "logic integration-account batch-configuration show",
)
class Show(AAZCommand):
    """Show a batch configuration for an integration account.

    :example: Show batch configuration
        az logic integration-account batch-configuration show -g rg -n batch --integration-account-name name
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/batchconfigurations/{}", "2019-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.batch_configuration_name = AAZStrArg(
            options=["-n", "--name", "--batch-configuration-name"],
            help="The batch configuration name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.integration_account_name = AAZStrArg(
            options=["--integration-account-name"],
            help="The integration account name.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountBatchConfigurationsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountBatchConfigurationsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/batchConfigurations/{batchConfigurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "batchConfigurationName", self.ctx.args.batch_configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.batch_group_name = AAZStrType(
                serialized_name="batchGroupName",
                flags={"required": True},
            )
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
            )
            properties.metadata = AAZFreeFormDictType()
            properties.release_criteria = AAZObjectType(
                serialized_name="releaseCriteria",
                flags={"required": True},
            )

            release_criteria = cls._schema_on_200.properties.release_criteria
            release_criteria.batch_size = AAZIntType(
                serialized_name="batchSize",
            )
            release_criteria.message_count = AAZIntType(
                serialized_name="messageCount",
            )
            release_criteria.recurrence = AAZObjectType()

            recurrence = cls._schema_on_200.properties.release_criteria.recurrence
            recurrence.end_time = AAZStrType(
                serialized_name="endTime",
            )
            recurrence.frequency = AAZStrType()
            recurrence.interval = AAZIntType()
            recurrence.schedule = AAZObjectType()
            recurrence.start_time = AAZStrType(
                serialized_name="startTime",
            )
            recurrence.time_zone = AAZStrType(
                serialized_name="timeZone",
            )

            schedule = cls._schema_on_200.properties.release_criteria.recurrence.schedule
            schedule.hours = AAZListType()
            schedule.minutes = AAZListType()
            schedule.month_days = AAZListType(
                serialized_name="monthDays",
            )
            schedule.monthly_occurrences = AAZListType(
                serialized_name="monthlyOccurrences",
            )
            schedule.week_days = AAZListType(
                serialized_name="weekDays",
            )

            hours = cls._schema_on_200.properties.release_criteria.recurrence.schedule.hours
            hours.Element = AAZIntType()

            minutes = cls._schema_on_200.properties.release_criteria.recurrence.schedule.minutes
            minutes.Element = AAZIntType()

            month_days = cls._schema_on_200.properties.release_criteria.recurrence.schedule.month_days
            month_days.Element = AAZIntType()

            monthly_occurrences = cls._schema_on_200.properties.release_criteria.recurrence.schedule.monthly_occurrences
            monthly_occurrences.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.release_criteria.recurrence.schedule.monthly_occurrences.Element
            _element.day = AAZStrType()
            _element.occurrence = AAZIntType()

            week_days = cls._schema_on_200.properties.release_criteria.recurrence.schedule.week_days
            week_days.Element = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
