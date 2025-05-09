# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1892
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
                    tenant_domain_name = '', 
                    provider = 'Bamboo', 
                    bamboo_auth_params = visier_api_data_in.models.designer/bamboo_auth_params_dto.designer.BambooAuthParamsDTO(
                        access_key = '', 
                        tenant_domain_name = '', ), 
                    greenhouse_auth_params = visier_api_data_in.models.designer/greenhouse_auth_params_dto.designer.GreenhouseAuthParamsDTO(
                        api_key = '', ), 
                    google_sheets_auth_params = visier_api_data_in.models.designer/google_sheets_auth_params_dto.designer.GoogleSheetsAuthParamsDTO(
                        auth_code = '', 
                        configuration = '', 
                        client_id = '', 
                        client_secret = '', ), 
                    jira_auth_params = visier_api_data_in.models.designer/jira_auth_params_dto.designer.JiraAuthParamsDTO(
                        api_token = '', 
                        host_name = '', 
                        connect_params = visier_api_data_in.models.designer/jira_connect_params_dto.designer.JiraConnectParamsDTO(
                            app_key = '', 
                            client_key = '', 
                            shared_secret = '', ), ), 
                    lever_auth_params = visier_api_data_in.models.designer/lever_auth_params_dto.designer.LeverAuthParamsDTO(
                        api_key = '', ), 
                    namely_auth_params = visier_api_data_in.models.designer/namely_auth_params_dto.designer.NamelyAuthParamsDTO(
                        auth_code = '', ), 
                    qualtrics_auth_params = visier_api_data_in.models.designer/qualtrics_auth_params_dto.designer.QualtricsAuthParamsDTO(
                        api_token = '', 
                        data_center_id = '', ), 
                    salesforce_auth_params = visier_api_data_in.models.designer/salesforce_auth_params_dto.designer.SalesforceAuthParamsDTO(
                        refresh_token = '', 
                        client_id = '', ), 
                    ultimate_auth_params = visier_api_data_in.models.designer/ultimate_auth_params_dto.designer.UltimateAuthParamsDTO(
                        host_domain_name = '', 
                        api_key = '', 
                        username = '', 
                        password = '', 
                        user_access_key = '', ), 
                    workday_auth_params = visier_api_data_in.models.designer/workday_auth_params_dto.designer.WorkdayAuthParamsDTO(
                        user_id = '', 
                        domain_name = '', 
                        implementation_name = '', 
                        password = '', 
                        o_auth = visier_api_data_in.models.designer/workday_o_auth_params_dto.designer.WorkdayOAuthParamsDTO(
                            api_client_id = '', 
                            public_x509_cert = '', 
                            private_x509_key = '', ), 
                        ref_token = visier_api_data_in.models.designer/workday_refresh_token_params_dto.designer.WorkdayRefreshTokenParamsDTO(
                            api_client_id = '', 
                            client_secret = '', 
                            refresh_token = '', ), 
                        integration_system_id = '', 
                        api_key = '', ), 
                    icims_auth_params = visier_api_data_in.models.designer/icims_auth_params_dto.designer.IcimsAuthParamsDTO(
                        customer_id = '', 
                        username = '', 
                        password = '', 
                        client_id = '', 
                        client_secret = '', 
                        region = 'US', ), 
                    service_now_auth_params = visier_api_data_in.models.designer/service_now_auth_params_dto.designer.ServiceNowAuthParamsDTO(
                        host_domain_name = '', 
                        username = '', 
                        password = '', ), 
                    jdbc_auth_params = visier_api_data_in.models.designer/jdbc_auth_params_dto.designer.JdbcAuthParamsDTO(
                        jdbc_connect_string = '', 
                        username = '', 
                        password = '', ), 
                    s3_auth_params = visier_api_data_in.models.designer/basic_s3_auth_params_dto.designer.BasicS3AuthParamsDTO(
                        bucket_name = '', 
                        bucket_region = '', 
                        access_key = '', 
                        secret_key = '', 
                        path = '', ), 
                    internal_s3_auth_params = visier_api_data_in.models.designer/internal_s3_auth_params_dto.designer.InternalS3AuthParamsDTO(
                        bucket_name = '', 
                        path = '', ), 
                    copy_s3_auth_params = visier_api_data_in.models.designer/copy_s3_auth_params_dto.designer.CopyS3AuthParamsDTO(
                        iam_role = '', ), 
                    redshift_auth_params = visier_api_data_in.models.designer/redshift_auth_params_dto.designer.RedshiftAuthParamsDTO(
                        endpoint = '', 
                        port = '', 
                        database = '', 
                        username = '', 
                        password = '', 
                        table_prefix = '', 
                        schema = '', ), 
                    snowflake_auth_params = visier_api_data_in.models.designer/snowflake_auth_params_dto.designer.SnowflakeAuthParamsDTO(
                        account_identifier = '', 
                        database = '', 
                        schema = '', 
                        username = '', 
                        password = '', 
                        warehouse = '', 
                        private_key = '', ), 
                    big_query_auth_params = visier_api_data_in.models.designer/big_query_auth_params_dto.designer.BigQueryAuthParamsDTO(
                        project_id = '', 
                        dataset_location = '', 
                        refresh_token = '', 
                        client_id = '', 
                        client_secret = '', 
                        default_dataset = '', 
                        service_account_params = visier_api_data_in.models.designer/big_query_service_account_params_dto.designer.BigQueryServiceAccountParamsDTO(
                            service_account_email = '', 
                            private_key = '', ), ), 
                    sql_server_auth_params = visier_api_data_in.models.designer/sql_server_auth_params_dto.designer.SqlServerAuthParamsDTO(
                        host = '', 
                        port = '', 
                        username = '', 
                        password = '', 
                        database = '', ), 
                    dimensions_auth_params = visier_api_data_in.models.designer/dimensions_auth_params_dto.designer.DimensionsAuthParamsDTO(
                        app_key = '', 
                        client_id = '', 
                        client_secret = '', 
                        vanity_url = '', 
                        username = '', 
                        password = '', ), 
                    willow_auth_params = visier_api_data_in.models.designer/willow_auth_params_dto.designer.WillowAuthParamsDTO(
                        api_token = '', 
                        host_name = '', ), 
                    empty_auth_params = visier_api_data_in.models.designer/empty_auth_params_dto.designer.EmptyAuthParamsDTO(), 
                    success_factors_auth_params = visier_api_data_in.models.designer/success_factors_auth_params_dto.designer.SuccessFactorsAuthParamsDTO(
                        host_domain_name = '', 
                        company_id = '', 
                        username = '', 
                        password = '', ), 
                    fusion_auth_params = visier_api_data_in.models.designer/fusion_auth_params_dto.designer.FusionAuthParamsDTO(
                        username = '', 
                        password = '', 
                        host_domain_name = '', ), 
                    adp_auth_params = visier_api_data_in.models.designer/adp_auth_params_dto.designer.AdpAuthParamsDTO(
                        auth_code = '', ), 
                    medallia_auth_params = visier_api_data_in.models.designer/medallia_auth_params_dto.designer.MedalliaAuthParamsDTO(
                        tenant_domain_name = '', 
                        instance_url = '', 
                        client_id = '', 
                        client_secret = '', ), 
                    salesforce_v2_auth_params = visier_api_data_in.models.designer/salesforce_v2_auth_params_dto.designer.SalesforceV2AuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        login_host = '', ), 
                    gong_auth_params = visier_api_data_in.models.designer/gong_auth_params_dto.designer.GongAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', ), 
                    zoom_auth_params = visier_api_data_in.models.designer/zoom_auth_params_dto.designer.ZoomAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', ), 
                    dayforce_v2_auth_params = visier_api_data_in.models.designer/dayforce_v2_auth_params_dto.designer.DayforceV2AuthParamsDTO(
                        username = '', 
                        password = '', 
                        company_id = '', 
                        token_host = '', 
                        host_domain_name = '', ), 
                    slack_auth_params = visier_api_data_in.models.designer/slack_auth_params_dto.designer.SlackAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', ), 
                    my_sql_auth_params = visier_api_data_in.models.designer/my_sql_auth_params_dto.designer.MySqlAuthParamsDTO(
                        host = '', 
                        port = '', 
                        username = '', 
                        password = '', 
                        database = '', 
                        ssl_mode = '', ), 
                    workday_raas_auth_params = visier_api_data_in.models.designer/workday_raas_auth_params_dto.designer.WorkdayRaasAuthParamsDTO(
                        user_id = '', 
                        domain_name = '', 
                        implementation_name = '', 
                        password = '', 
                        test_report_url = '', ), 
                    ms365_auth_params = visier_api_data_in.models.designer/microsoft365_auth_params_dto.designer.Microsoft365AuthParamsDTO(
                        o_auth_tenant_id = '', 
                        client_id = '', 
                        client_secret = '', 
                        privacy_mode = '', ), 
                    google_workspace_auth_params = visier_api_data_in.models.designer/google_workspace_auth_params_dto.designer.GoogleWorkspaceAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        service_account = '', 
                        privacy_mode = '', ), 
                    oracle_db_auth_params = visier_api_data_in.models.designer/oracle_db_auth_params_dto.designer.OracleDbAuthParamsDTO(
                        host = '', 
                        port = '', 
                        username = '', 
                        password = '', 
                        service_name = '', ), 
                    service_now_v2_auth_params = visier_api_data_in.models.designer/service_now_v2_auth_params_dto.designer.ServiceNowV2AuthParamsDTO(
                        host_domain_name = '', 
                        client_id = '', 
                        client_secret = '', 
                        auth_code = '', 
                        alternate_domain = '', ), 
                    databricks_auth_params = visier_api_data_in.models.designer/databricks_auth_params_dto.designer.DatabricksAuthParamsDTO(
                        share_credentials_version = '', 
                        bearer_token = '', 
                        endpoint = '', 
                        expiration_time = '', ), 
                    has_updates = True, 
                    auth_context = 'DefaultDataExtraction', ),
                data_provider_basic_information = visier_api_data_in.models.designer/data_provider_basic_information_dto.designer.DataProviderBasicInformationDTO(
                    display_name = '', 
                    description = '', ),
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
