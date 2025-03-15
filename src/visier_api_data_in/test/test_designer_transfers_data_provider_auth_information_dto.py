# coding: utf-8

"""
    Visier Data In APIs

    Visier APIs for sending data to Visier and running data load jobs.

    The version of the OpenAPI document: 22222222.99201.1793
    Contact: alpine@visier.com

    Please note that this SDK is currently in beta.
    Functionality and behavior may change in future releases.
    We encourage you to provide feedback and report any issues encountered during your use.
"""  # noqa: E501


import unittest

import visier_api_data_in.models
from visier_api_data_in.models.designer_transfers_data_provider_auth_information_dto import DesignerTransfersDataProviderAuthInformationDTO

class TestDesignerTransfersDataProviderAuthInformationDTO(unittest.TestCase):
    """DesignerTransfersDataProviderAuthInformationDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DesignerTransfersDataProviderAuthInformationDTO:
        """Test DesignerTransfersDataProviderAuthInformationDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """

        if include_optional:
            return DesignerTransfersDataProviderAuthInformationDTO(
                data_provider_auth_params = visier_api_data_in.models.designer/transfers/data_provider_auth_params_dto.designer.transfers.DataProviderAuthParamsDTO(
                    adp_auth_params = visier_api_data_in.models.designer/transfers/adp_auth_params_dto.designer.transfers.AdpAuthParamsDTO(
                        auth_code = '', ), 
                    auth_context = 'DefaultDataExtraction', 
                    bamboo_auth_params = visier_api_data_in.models.designer/transfers/bamboo_auth_params_dto.designer.transfers.BambooAuthParamsDTO(
                        access_key = '', 
                        tenant_domain_name = '', ), 
                    big_query_auth_params = visier_api_data_in.models.designer/transfers/big_query_auth_params_dto.designer.transfers.BigQueryAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        dataset_location = '', 
                        default_dataset = '', 
                        project_id = '', 
                        refresh_token = '', 
                        service_account_params = visier_api_data_in.models.designer/transfers/big_query_service_account_params_dto.designer.transfers.BigQueryServiceAccountParamsDTO(
                            private_key = '', 
                            service_account_email = '', ), ), 
                    copy_s3_auth_params = visier_api_data_in.models.designer/transfers/copy_s3_auth_params_dto.designer.transfers.CopyS3AuthParamsDTO(
                        iam_role = '', ), 
                    dayforce_v2_auth_params = visier_api_data_in.models.designer/transfers/dayforce_v2_auth_params_dto.designer.transfers.DayforceV2AuthParamsDTO(
                        company_id = '', 
                        host_domain_name = '', 
                        password = '', 
                        token_host = '', 
                        username = '', ), 
                    dimensions_auth_params = visier_api_data_in.models.designer/transfers/dimensions_auth_params_dto.designer.transfers.DimensionsAuthParamsDTO(
                        app_key = '', 
                        client_id = '', 
                        client_secret = '', 
                        password = '', 
                        username = '', 
                        vanity_url = '', ), 
                    empty_auth_params = visier_api_data_in.models.designer/transfers/empty_auth_params_dto.designer.transfers.EmptyAuthParamsDTO(), 
                    fusion_auth_params = visier_api_data_in.models.designer/transfers/fusion_auth_params_dto.designer.transfers.FusionAuthParamsDTO(
                        host_domain_name = '', 
                        password = '', 
                        username = '', ), 
                    gong_auth_params = visier_api_data_in.models.designer/transfers/gong_auth_params_dto.designer.transfers.GongAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', ), 
                    google_sheets_auth_params = visier_api_data_in.models.designer/transfers/google_sheets_auth_params_dto.designer.transfers.GoogleSheetsAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        configuration = '', ), 
                    google_workspace_auth_params = visier_api_data_in.models.designer/transfers/google_workspace_auth_params_dto.designer.transfers.GoogleWorkspaceAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        privacy_mode = '', 
                        service_account = '', ), 
                    greenhouse_auth_params = visier_api_data_in.models.designer/transfers/greenhouse_auth_params_dto.designer.transfers.GreenhouseAuthParamsDTO(
                        api_key = '', ), 
                    has_updates = True, 
                    icims_auth_params = visier_api_data_in.models.designer/transfers/icims_auth_params_dto.designer.transfers.IcimsAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        customer_id = '', 
                        password = '', 
                        region = 'US', 
                        username = '', ), 
                    internal_s3_auth_params = visier_api_data_in.models.designer/transfers/internal_s3_auth_params_dto.designer.transfers.InternalS3AuthParamsDTO(
                        bucket_name = '', 
                        path = '', ), 
                    jdbc_auth_params = visier_api_data_in.models.designer/transfers/jdbc_auth_params_dto.designer.transfers.JdbcAuthParamsDTO(
                        jdbc_connect_string = '', 
                        password = '', 
                        username = '', ), 
                    jira_auth_params = visier_api_data_in.models.designer/transfers/jira_auth_params_dto.designer.transfers.JiraAuthParamsDTO(
                        api_token = '', 
                        connect_params = visier_api_data_in.models.designer/transfers/jira_connect_params_dto.designer.transfers.JiraConnectParamsDTO(
                            app_key = '', 
                            client_key = '', 
                            shared_secret = '', ), 
                        host_name = '', ), 
                    lever_auth_params = visier_api_data_in.models.designer/transfers/lever_auth_params_dto.designer.transfers.LeverAuthParamsDTO(
                        api_key = '', ), 
                    medallia_auth_params = visier_api_data_in.models.designer/transfers/medallia_auth_params_dto.designer.transfers.MedalliaAuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        instance_url = '', 
                        tenant_domain_name = '', ), 
                    ms365_auth_params = visier_api_data_in.models.designer/transfers/microsoft365_auth_params_dto.designer.transfers.Microsoft365AuthParamsDTO(
                        client_id = '', 
                        client_secret = '', 
                        o_auth_tenant_id = '', 
                        privacy_mode = '', ), 
                    my_sql_auth_params = visier_api_data_in.models.designer/transfers/my_sql_auth_params_dto.designer.transfers.MySqlAuthParamsDTO(
                        database = '', 
                        host = '', 
                        password = '', 
                        port = '', 
                        ssl_mode = '', 
                        username = '', ), 
                    namely_auth_params = visier_api_data_in.models.designer/transfers/namely_auth_params_dto.designer.transfers.NamelyAuthParamsDTO(
                        auth_code = '', ), 
                    oracle_db_auth_params = visier_api_data_in.models.designer/transfers/oracle_db_auth_params_dto.designer.transfers.OracleDbAuthParamsDTO(
                        host = '', 
                        password = '', 
                        port = '', 
                        service_name = '', 
                        username = '', ), 
                    provider = 'Bamboo', 
                    qualtrics_auth_params = visier_api_data_in.models.designer/transfers/qualtrics_auth_params_dto.designer.transfers.QualtricsAuthParamsDTO(
                        api_token = '', 
                        data_center_id = '', ), 
                    redshift_auth_params = visier_api_data_in.models.designer/transfers/redshift_auth_params_dto.designer.transfers.RedshiftAuthParamsDTO(
                        database = '', 
                        endpoint = '', 
                        password = '', 
                        port = '', 
                        schema = '', 
                        table_prefix = '', 
                        username = '', ), 
                    s3_auth_params = visier_api_data_in.models.designer/transfers/basic_s3_auth_params_dto.designer.transfers.BasicS3AuthParamsDTO(
                        access_key = '', 
                        bucket_name = '', 
                        bucket_region = '', 
                        path = '', 
                        secret_key = '', ), 
                    salesforce_auth_params = visier_api_data_in.models.designer/transfers/salesforce_auth_params_dto.designer.transfers.SalesforceAuthParamsDTO(
                        client_id = '', 
                        refresh_token = '', ), 
                    salesforce_v2_auth_params = visier_api_data_in.models.designer/transfers/salesforce_v2_auth_params_dto.designer.transfers.SalesforceV2AuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        login_host = '', ), 
                    service_now_auth_params = visier_api_data_in.models.designer/transfers/service_now_auth_params_dto.designer.transfers.ServiceNowAuthParamsDTO(
                        host_domain_name = '', 
                        password = '', 
                        username = '', ), 
                    service_now_v2_auth_params = visier_api_data_in.models.designer/transfers/service_now_v2_auth_params_dto.designer.transfers.ServiceNowV2AuthParamsDTO(
                        alternate_domain = '', 
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', 
                        host_domain_name = '', ), 
                    slack_auth_params = visier_api_data_in.models.designer/transfers/slack_auth_params_dto.designer.transfers.SlackAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', ), 
                    snowflake_auth_params = visier_api_data_in.models.designer/transfers/snowflake_auth_params_dto.designer.transfers.SnowflakeAuthParamsDTO(
                        account_identifier = '', 
                        database = '', 
                        password = '', 
                        private_key = '', 
                        schema = '', 
                        username = '', 
                        warehouse = '', ), 
                    sql_server_auth_params = visier_api_data_in.models.designer/transfers/sql_server_auth_params_dto.designer.transfers.SqlServerAuthParamsDTO(
                        database = '', 
                        host = '', 
                        password = '', 
                        port = '', 
                        username = '', ), 
                    success_factors_auth_params = visier_api_data_in.models.designer/transfers/success_factors_auth_params_dto.designer.transfers.SuccessFactorsAuthParamsDTO(
                        company_id = '', 
                        host_domain_name = '', 
                        o_auth = visier_api_data_in.models.designer/transfers/success_factors_o_auth_params_dto.designer.transfers.SuccessFactorsOAuthParamsDTO(
                            api_key = '', 
                            private_x509_key = '', 
                            public_x509_cert = '', ), 
                        password = '', 
                        username = '', ), 
                    tenant_domain_name = '', 
                    ultimate_auth_params = visier_api_data_in.models.designer/transfers/ultimate_auth_params_dto.designer.transfers.UltimateAuthParamsDTO(
                        api_key = '', 
                        host_domain_name = '', 
                        password = '', 
                        user_access_key = '', 
                        username = '', ), 
                    willow_auth_params = visier_api_data_in.models.designer/transfers/willow_auth_params_dto.designer.transfers.WillowAuthParamsDTO(
                        api_token = '', 
                        host_name = '', ), 
                    workday_auth_params = visier_api_data_in.models.designer/transfers/workday_auth_params_dto.designer.transfers.WorkdayAuthParamsDTO(
                        api_key = '', 
                        domain_name = '', 
                        implementation_name = '', 
                        integration_system_id = '', 
                        password = '', 
                        ref_token = visier_api_data_in.models.designer/transfers/workday_refresh_token_params_dto.designer.transfers.WorkdayRefreshTokenParamsDTO(
                            api_client_id = '', 
                            client_secret = '', 
                            refresh_token = '', ), 
                        user_id = '', ), 
                    workday_raas_auth_params = visier_api_data_in.models.designer/transfers/workday_raas_auth_params_dto.designer.transfers.WorkdayRaasAuthParamsDTO(
                        domain_name = '', 
                        implementation_name = '', 
                        password = '', 
                        test_report_url = '', 
                        user_id = '', ), 
                    zoom_auth_params = visier_api_data_in.models.designer/transfers/zoom_auth_params_dto.designer.transfers.ZoomAuthParamsDTO(
                        auth_code = '', 
                        client_id = '', 
                        client_secret = '', ), ),
                data_provider_basic_information = visier_api_data_in.models.designer/transfers/data_provider_basic_information_dto.designer.transfers.DataProviderBasicInformationDTO(
                    description = '', 
                    display_name = '', ),
                data_provider_metadata = visier_api_data_in.models.designer/transfers/data_provider_basic_metadata_dto.designer.transfers.DataProviderBasicMetadataDTO(
                    can_children_inherit = True, )
            )
        else:
            return DesignerTransfersDataProviderAuthInformationDTO(
        )

    def testDesignerTransfersDataProviderAuthInformationDTO(self):
        """Test DesignerTransfersDataProviderAuthInformationDTO"""
        def validate_instance(instance):
            DesignerTransfersDataProviderAuthInformationDTO.model_validate(inst_req_only)
            instance_deserialized = DesignerTransfersDataProviderAuthInformationDTO.from_dict(instance.to_dict())
            assert instance == instance_deserialized

        inst_req_only = self.make_instance(include_optional=False)
        validate_instance(inst_req_only)

        inst_req_and_optional = self.make_instance(include_optional=True)
        validate_instance(inst_req_and_optional)

if __name__ == '__main__':
    unittest.main()
