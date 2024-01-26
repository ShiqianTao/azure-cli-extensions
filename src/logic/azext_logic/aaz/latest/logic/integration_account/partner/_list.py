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
    "logic integration-account partner list",
)
class List(AAZCommand):
    """List integration account partners.

    :example: List partner
        az logic integration-account partner list -g rg --integration-account-name name
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/partners", "2019-05-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.integration_account_name = AAZStrArg(
            options=["--integration-account-name"],
            help="The integration account name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply on the operation. Options for filters include: PartnerType.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="The number of items to be included in the result.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountPartnersList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class IntegrationAccountPartnersList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners",
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
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
                flags={"read_only": True},
            )
            properties.content = AAZObjectType(
                flags={"required": True},
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
                flags={"read_only": True},
            )
            properties.metadata = AAZFreeFormDictType()
            properties.partner_type = AAZStrType(
                serialized_name="partnerType",
                flags={"required": True},
            )

            content = cls._schema_on_200.value.Element.properties.content
            content.b2b = AAZObjectType()

            b2b = cls._schema_on_200.value.Element.properties.content.b2b
            b2b.business_identities = AAZListType(
                serialized_name="businessIdentities",
            )

            business_identities = cls._schema_on_200.value.Element.properties.content.b2b.business_identities
            business_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.content.b2b.business_identities.Element
            _element.qualifier = AAZStrType(
                flags={"required": True},
            )
            _element.value = AAZStrType(
                flags={"required": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
