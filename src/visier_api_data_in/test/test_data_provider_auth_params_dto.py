# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1614
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.data_provider_auth_params_dto import DataProviderAuthParamsDTO

class TestDataProviderAuthParamsDTO(unittest.TestCase):
    """DataProviderAuthParamsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataProviderAuthParamsDTO:
        """Test DataProviderAuthParamsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DataProviderAuthParamsDTO(
                adp_auth_params = visier_api_data_in.models.adp_auth_params_dto.AdpAuthParamsDTO(
                    auth_code = '', ),
                auth_context = 'DefaultDataExtraction',
                bamboo_auth_params = visier_api_data_in.models.bamboo_auth_params_dto.BambooAuthParamsDTO(
                    access_key = '', 
                    tenant_domain_name = '', ),
                big_query_auth_params = visier_api_data_in.models.big_query_auth_params_dto.BigQueryAuthParamsDTO(
                    client_id = '', 
                    client_secret = '', 
                    dataset_location = '', 
                    default_dataset = '', 
                    project_id = '', 
                    refresh_token = '', 
                    service_account_params = visier_api_data_in.models.big_query_service_account_params_dto.BigQueryServiceAccountParamsDTO(
                        private_key = '', 
                        service_account_email = '', ), ),
                copy_s3_auth_params = visier_api_data_in.models.copy_s3_auth_params_dto.CopyS3AuthParamsDTO(
                    iam_role = '', ),
                dayforce_v2_auth_params = visier_api_data_in.models.dayforce_v2_auth_params_dto.DayforceV2AuthParamsDTO(
                    company_id = '', 
                    host_domain_name = '', 
                    password = '', 
                    token_host = '', 
                    username = '', ),
                dimensions_auth_params = visier_api_data_in.models.dimensions_auth_params_dto.DimensionsAuthParamsDTO(
                    app_key = '', 
                    client_id = '', 
                    client_secret = '', 
                    password = '', 
                    username = '', 
                    vanity_url = '', ),
                empty_auth_params = {},
                fusion_auth_params = visier_api_data_in.models.fusion_auth_params_dto.FusionAuthParamsDTO(
                    host_domain_name = '', 
                    password = '', 
                    username = '', ),
                gong_auth_params = visier_api_data_in.models.gong_auth_params_dto.GongAuthParamsDTO(
                    client_id = '', 
                    client_secret = '', ),
                google_sheets_auth_params = visier_api_data_in.models.google_sheets_auth_params_dto.GoogleSheetsAuthParamsDTO(
                    auth_code = '', 
                    client_id = '', 
                    client_secret = '', 
                    configuration = '', ),
                google_workspace_auth_params = visier_api_data_in.models.google_workspace_auth_params_dto.GoogleWorkspaceAuthParamsDTO(
                    auth_code = '', 
                    client_id = '', 
                    client_secret = '', 
                    privacy_mode = '', 
                    service_account = '', ),
                greenhouse_auth_params = visier_api_data_in.models.greenhouse_auth_params_dto.GreenhouseAuthParamsDTO(
                    api_key = '', ),
                has_updates = True,
                icims_auth_params = visier_api_data_in.models.icims_auth_params_dto.IcimsAuthParamsDTO(
                    client_id = '', 
                    client_secret = '', 
                    customer_id = '', 
                    password = '', 
                    region = 'US', 
                    username = '', ),
                internal_s3_auth_params = visier_api_data_in.models.internal_s3_auth_params_dto.InternalS3AuthParamsDTO(
                    bucket_name = '', 
                    path = '', ),
                jdbc_auth_params = visier_api_data_in.models.jdbc_auth_params_dto.JdbcAuthParamsDTO(
                    jdbc_connect_string = '', 
                    password = '', 
                    username = '', ),
                jira_auth_params = visier_api_data_in.models.jira_auth_params_dto.JiraAuthParamsDTO(
                    api_token = '', 
                    connect_params = visier_api_data_in.models.jira_connect_params_dto.JiraConnectParamsDTO(
                        app_key = '', 
                        client_key = '', 
                        shared_secret = '', ), 
                    host_name = '', ),
                lever_auth_params = visier_api_data_in.models.lever_auth_params_dto.LeverAuthParamsDTO(
                    api_key = '', ),
                medallia_auth_params = visier_api_data_in.models.medallia_auth_params_dto.MedalliaAuthParamsDTO(
                    client_id = '', 
                    client_secret = '', 
                    instance_url = '', 
                    tenant_domain_name = '', ),
                ms365_auth_params = visier_api_data_in.models.microsoft365_auth_params_dto.Microsoft365AuthParamsDTO(
                    client_id = '', 
                    client_secret = '', 
                    o_auth_tenant_id = '', 
                    privacy_mode = '', ),
                my_sql_auth_params = visier_api_data_in.models.my_sql_auth_params_dto.MySqlAuthParamsDTO(
                    database = '', 
                    host = '', 
                    password = '', 
                    port = '', 
                    ssl_mode = '', 
                    username = '', ),
                namely_auth_params = visier_api_data_in.models.namely_auth_params_dto.NamelyAuthParamsDTO(
                    auth_code = '', ),
                oracle_db_auth_params = visier_api_data_in.models.oracle_db_auth_params_dto.OracleDbAuthParamsDTO(
                    host = '', 
                    password = '', 
                    port = '', 
                    service_name = '', 
                    username = '', ),
                provider = 'Bamboo',
                qualtrics_auth_params = visier_api_data_in.models.qualtrics_auth_params_dto.QualtricsAuthParamsDTO(
                    api_token = '', 
                    data_center_id = '', ),
                redshift_auth_params = visier_api_data_in.models.redshift_auth_params_dto.RedshiftAuthParamsDTO(
                    database = '', 
                    endpoint = '', 
                    password = '', 
                    port = '', 
                    schema = '', 
                    table_prefix = '', 
                    username = '', ),
                s3_auth_params = visier_api_data_in.models.basic_s3_auth_params_dto.BasicS3AuthParamsDTO(
                    access_key = '', 
                    bucket_name = '', 
                    bucket_region = '', 
                    path = '', 
                    secret_key = '', ),
                salesforce_auth_params = visier_api_data_in.models.salesforce_auth_params_dto.SalesforceAuthParamsDTO(
                    client_id = '', 
                    refresh_token = '', ),
                salesforce_v2_auth_params = visier_api_data_in.models.salesforce_v2_auth_params_dto.SalesforceV2AuthParamsDTO(
                    auth_code = '', 
                    client_id = '', 
                    client_secret = '', 
                    login_host = '', ),
                service_now_auth_params = visier_api_data_in.models.service_now_auth_params_dto.ServiceNowAuthParamsDTO(
                    host_domain_name = '', 
                    password = '', 
                    username = '', ),
                service_now_v2_auth_params = visier_api_data_in.models.service_now_v2_auth_params_dto.ServiceNowV2AuthParamsDTO(
                    alternate_domain = '', 
                    auth_code = '', 
                    client_id = '', 
                    client_secret = '', 
                    host_domain_name = '', ),
                slack_auth_params = visier_api_data_in.models.slack_auth_params_dto.SlackAuthParamsDTO(
                    auth_code = '', 
                    client_id = '', 
                    client_secret = '', ),
                snowflake_auth_params = visier_api_data_in.models.snowflake_auth_params_dto.SnowflakeAuthParamsDTO(
                    account_identifier = '', 
                    database = '', 
                    password = '', 
                    private_key = '', 
                    schema = '', 
                    username = '', 
                    warehouse = '', ),
                sql_server_auth_params = visier_api_data_in.models.sql_server_auth_params_dto.SqlServerAuthParamsDTO(
                    database = '', 
                    host = '', 
                    password = '', 
                    port = '', 
                    username = '', ),
                success_factors_auth_params = visier_api_data_in.models.success_factors_auth_params_dto.SuccessFactorsAuthParamsDTO(
                    company_id = '', 
                    host_domain_name = '', 
                    o_auth = visier_api_data_in.models.success_factors_o_auth_params_dto.SuccessFactorsOAuthParamsDTO(
                        api_key = '', 
                        private_x509_key = '', 
                        public_x509_cert = '', ), 
                    password = '', 
                    username = '', ),
                tenant_domain_name = '',
                ultimate_auth_params = visier_api_data_in.models.ultimate_auth_params_dto.UltimateAuthParamsDTO(
                    api_key = '', 
                    host_domain_name = '', 
                    password = '', 
                    user_access_key = '', 
                    username = '', ),
                willow_auth_params = visier_api_data_in.models.willow_auth_params_dto.WillowAuthParamsDTO(
                    api_token = '', 
                    host_name = '', ),
                workday_auth_params = visier_api_data_in.models.workday_auth_params_dto.WorkdayAuthParamsDTO(
                    api_key = '', 
                    domain_name = '', 
                    implementation_name = '', 
                    integration_system_id = '', 
                    o_auth = visier_api_data_in.models.workday_o_auth_params_dto.WorkdayOAuthParamsDTO(
                        api_client_id = '', 
                        private_x509_key = '', 
                        public_x509_cert = '', ), 
                    password = '', 
                    ref_token = visier_api_data_in.models.workday_refresh_token_params_dto.WorkdayRefreshTokenParamsDTO(
                        api_client_id = '', 
                        client_secret = '', 
                        refresh_token = '', ), 
                    user_id = '', ),
                workday_raas_auth_params = visier_api_data_in.models.workday_raas_auth_params_dto.WorkdayRaasAuthParamsDTO(
                    domain_name = '', 
                    implementation_name = '', 
                    password = '', 
                    test_report_url = '', 
                    user_id = '', ),
                zoom_auth_params = visier_api_data_in.models.zoom_auth_params_dto.ZoomAuthParamsDTO(
                    auth_code = '', 
                    client_id = '', 
                    client_secret = '', )
            )
        else:
            return DataProviderAuthParamsDTO(
        )

    def testDataProviderAuthParamsDTO(self):
        """Test DataProviderAuthParamsDTO"""
        def validate_instance(instance):
            DataProviderAuthParamsDTO.model_validate(inst_req_only)
            instance_deserialized = DataProviderAuthParamsDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
