# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1830
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.designer_data_provider_auth_information_dto import DesignerDataProviderAuthInformationDTO

class TestDesignerDataProviderAuthInformationDTO(unittest.TestCase):
    """DesignerDataProviderAuthInformationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerDataProviderAuthInformationDTO:
        """Test DesignerDataProviderAuthInformationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerDataProviderAuthInformationDTO(
                data_provider_auth_params = visier_api_data_in.models.designer/data_provider_auth_params_dto.designer.DataProviderAuthParamsDTO(
                    adp_auth_params = visier_api_data_in.models.designer/adp_auth_params_dto.designer.AdpAuthParamsDTO(
                        auth_code = '', ), 
                    auth_context = 'DefaultDataExtraction', 
                    bamboo_auth_params = visier_api_data_in.models.designer/bamboo_auth_params_dto.designer.BambooAuthParamsDTO(
                        access_key = '', 
                        tenant_domain_name = '', ), 
                    big_query_auth_params = visier_api_data_in.models.designer/big_query_auth_params_dto.designer.BigQueryAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        dataset_location = '', 
                        default_dataset = '', 
                        project_id = '', 
                        refresh_token = '', 
                        service_account_params = visier_api_data_in.models.designer/big_query_service_account_params_dto.designer.BigQueryServiceAccountParamsDTO(
                            private_key = '', 
                            service_account_email = '', ), ), 
                    copy_s3_auth_params = visier_api_data_in.models.designer/copy_s3_auth_params_dto.designer.CopyS3AuthParamsDTO(
                        iam_role = '', ), 
                    dayforce_v2_auth_params = visier_api_data_in.models.designer/dayforce_v2_auth_params_dto.designer.DayforceV2AuthParamsDTO(
                        company_id = '', 
                        host_domain_name = '', 
                        password = '', 
                        token_host = '', 
                        username = '', ), 
                    dimensions_auth_params = visier_api_data_in.models.designer/dimensions_auth_params_dto.designer.DimensionsAuthParamsDTO(
                        app_key = '', 
                        client_id = '', 
                        client_secret = '', 
                        password = '', 
                        username = '', 
                        vanity_url = '', ), 
                    empty_auth_params = visier_api_data_in.models.designer/empty_auth_params_dto.designer.EmptyAuthParamsDTO(), 
                    fusion_auth_params = visier_api_data_in.models.designer/fusion_auth_params_dto.designer.FusionAuthParamsDTO(
                        host_domain_name = '', 
                        password = '', 
                        username = '', ), 
                    gong_auth_params = visier_api_data_in.models.designer/gong_auth_params_dto.designer.GongAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', ), 
                    google_sheets_auth_params = visier_api_data_in.models.designer/google_sheets_auth_params_dto.designer.GoogleSheetsAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        configuration = '', ), 
                    google_workspace_auth_params = visier_api_data_in.models.designer/google_workspace_auth_params_dto.designer.GoogleWorkspaceAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        privacy_mode = '', 
                        service_account = '', ), 
                    greenhouse_auth_params = visier_api_data_in.models.designer/greenhouse_auth_params_dto.designer.GreenhouseAuthParamsDTO(
                        api_key = '', ), 
                    has_updates = True, 
                    icims_auth_params = visier_api_data_in.models.designer/icims_auth_params_dto.designer.IcimsAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        customer_id = '', 
                        password = '', 
                        region = 'US', 
                        username = '', ), 
                    internal_s3_auth_params = visier_api_data_in.models.designer/internal_s3_auth_params_dto.designer.InternalS3AuthParamsDTO(
                        bucket_name = '', 
                        path = '', ), 
                    jdbc_auth_params = visier_api_data_in.models.designer/jdbc_auth_params_dto.designer.JdbcAuthParamsDTO(
                        jdbc_connect_string = '', 
                        password = '', 
                        username = '', ), 
                    jira_auth_params = visier_api_data_in.models.designer/jira_auth_params_dto.designer.JiraAuthParamsDTO(
                        api_token = '', 
                        connect_params = visier_api_data_in.models.designer/jira_connect_params_dto.designer.JiraConnectParamsDTO(
                            app_key = '', 
                            client_key = '', 
                            shared_secret = '', ), 
                        host_name = '', ), 
                    lever_auth_params = visier_api_data_in.models.designer/lever_auth_params_dto.designer.LeverAuthParamsDTO(
                        api_key = '', ), 
                    medallia_auth_params = visier_api_data_in.models.designer/medallia_auth_params_dto.designer.MedalliaAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        instance_url = '', 
                        tenant_domain_name = '', ), 
                    ms365_auth_params = visier_api_data_in.models.designer/microsoft365_auth_params_dto.designer.Microsoft365AuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        o_auth_tenant_id = '', 
                        privacy_mode = '', ), 
                    my_sql_auth_params = visier_api_data_in.models.designer/my_sql_auth_params_dto.designer.MySqlAuthParamsDTO(
                        database = '', 
                        host = '', 
                        password = '', 
                        port = '', 
                        ssl_mode = '', 
                        username = '', ), 
                    namely_auth_params = visier_api_data_in.models.designer/namely_auth_params_dto.designer.NamelyAuthParamsDTO(
                        auth_code = '', ), 
                    oracle_db_auth_params = visier_api_data_in.models.designer/oracle_db_auth_params_dto.designer.OracleDbAuthParamsDTO(
                        host = '', 
                        password = '', 
                        port = '', 
                        service_name = '', 
                        username = '', ), 
                    provider = 'Bamboo', 
                    qualtrics_auth_params = visier_api_data_in.models.designer/qualtrics_auth_params_dto.designer.QualtricsAuthParamsDTO(
                        api_token = '', 
                        data_center_id = '', ), 
                    redshift_auth_params = visier_api_data_in.models.designer/redshift_auth_params_dto.designer.RedshiftAuthParamsDTO(
                        database = '', 
                        endpoint = '', 
                        password = '', 
                        port = '', 
                        schema = '', 
                        table_prefix = '', 
                        username = '', ), 
                    s3_auth_params = visier_api_data_in.models.designer/basic_s3_auth_params_dto.designer.BasicS3AuthParamsDTO(
                        access_key = '', 
                        bucket_name = '', 
                        bucket_region = '', 
                        path = '', 
                        secret_key = '', ), 
                    salesforce_auth_params = visier_api_data_in.models.designer/salesforce_auth_params_dto.designer.SalesforceAuthParamsDTO(
                        client_id = '', 
                        refresh_token = '', ), 
                    salesforce_v2_auth_params = visier_api_data_in.models.designer/salesforce_v2_auth_params_dto.designer.SalesforceV2AuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        login_host = '', ), 
                    service_now_auth_params = visier_api_data_in.models.designer/service_now_auth_params_dto.designer.ServiceNowAuthParamsDTO(
                        host_domain_name = '', 
                        password = '', 
                        username = '', ), 
                    service_now_v2_auth_params = visier_api_data_in.models.designer/service_now_v2_auth_params_dto.designer.ServiceNowV2AuthParamsDTO(
                        alternate_domain = '', 
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        host_domain_name = '', ), 
                    slack_auth_params = visier_api_data_in.models.designer/slack_auth_params_dto.designer.SlackAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', ), 
                    snowflake_auth_params = visier_api_data_in.models.designer/snowflake_auth_params_dto.designer.SnowflakeAuthParamsDTO(
                        account_identifier = '', 
                        database = '', 
                        password = '', 
                        private_key = '', 
                        schema = '', 
                        username = '', 
                        warehouse = '', ), 
                    sql_server_auth_params = visier_api_data_in.models.designer/sql_server_auth_params_dto.designer.SqlServerAuthParamsDTO(
                        database = '', 
                        host = '', 
                        password = '', 
                        port = '', 
                        username = '', ), 
                    success_factors_auth_params = visier_api_data_in.models.designer/success_factors_auth_params_dto.designer.SuccessFactorsAuthParamsDTO(
                        company_id = '', 
                        host_domain_name = '', 
                        o_auth = visier_api_data_in.models.designer/success_factors_o_auth_params_dto.designer.SuccessFactorsOAuthParamsDTO(
                            api_key = '', 
                            private_x509_key = '', 
                            public_x509_cert = '', ), 
                        password = '', 
                        username = '', ), 
                    tenant_domain_name = '', 
                    ultimate_auth_params = visier_api_data_in.models.designer/ultimate_auth_params_dto.designer.UltimateAuthParamsDTO(
                        api_key = '', 
                        host_domain_name = '', 
                        password = '', 
                        user_access_key = '', 
                        username = '', ), 
                    willow_auth_params = visier_api_data_in.models.designer/willow_auth_params_dto.designer.WillowAuthParamsDTO(
                        api_token = '', 
                        host_name = '', ), 
                    workday_auth_params = visier_api_data_in.models.designer/workday_auth_params_dto.designer.WorkdayAuthParamsDTO(
                        api_key = '', 
                        domain_name = '', 
                        implementation_name = '', 
                        integration_system_id = '', 
                        password = '', 
                        ref_token = visier_api_data_in.models.designer/workday_refresh_token_params_dto.designer.WorkdayRefreshTokenParamsDTO(
                            api_client_id = '', 
                            client_secret = '', 
                            refresh_token = '', ), 
                        user_id = '', ), 
                    workday_raas_auth_params = visier_api_data_in.models.designer/workday_raas_auth_params_dto.designer.WorkdayRaasAuthParamsDTO(
                        domain_name = '', 
                        implementation_name = '', 
                        password = '', 
                        test_report_url = '', 
                        user_id = '', ), 
                    zoom_auth_params = visier_api_data_in.models.designer/zoom_auth_params_dto.designer.ZoomAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', ), ),
                data_provider_basic_information = visier_api_data_in.models.designer/data_provider_basic_information_dto.designer.DataProviderBasicInformationDTO(
                    description = '', 
                    display_name = '', ),
                data_provider_metadata = visier_api_data_in.models.designer/data_provider_basic_metadata_dto.designer.DataProviderBasicMetadataDTO(
                    can_children_inherit = True, )
            )
        else:
            return DesignerDataProviderAuthInformationDTO(
        )

    def testDesignerDataProviderAuthInformationDTO(self):
        """Test DesignerDataProviderAuthInformationDTO"""
        def validate_instance(instance):
            DesignerDataProviderAuthInformationDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerDataProviderAuthInformationDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
