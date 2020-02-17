!!! info "Jenkins Requirements"
    1. [java](https://jenkins.io/doc/administration/requirements/java/)
    1. [docker](https://docs.docker.com/get-docker/)

    Then follow [jenkins installation using docker](https://jenkins.io/doc/book/installing/#installing-docker) to install Jenkins on the localhost and choose "Install suggested plugins". After successful installation, one should be able to reach the [Jenkins Dashboard](http://localhost:8080) (8080 is default port).
    ![Image](../images/jenkins-ui.png)

!!! example "Setting Up Jenkins Pipeline"
    1. Login to Jenkins
    1. Click on " New Item"
    ![Image](../images/jenkins-new-item.png)
    1. Name you Project, select pipeline option and click "Ok"
    ![Image](../images/jenkins-pipeline-name.png)
    1. In the pipeline details, fill in the scm details as seen in the image below and click "Save".
    Everything default apart from:
        1. Repository Url: https://github.com/netfoundry/mop.git
        1. Script Path: pipeline/netfoundrydeploy2cloud.jenkinsfile
    ![Image](../images/jenkins-pipeline-option.png)
    1. Set up users for Azure API and NF MOP API access --
    [More on Credentials setup](https://jenkins.io/doc/book/using/using-credentials/)
    ![Image](../images/jenkins-creds.png)
    1. Run Jenkinsjob by selecting on the pipeline created in the previous step. Click on "Build with Parameters"
    ![Image](../images/jenkins-pipeline-build-with-parameters.png)
    1. Fill in the Azure Details and select the following:
        1. NF Environment, e.g. production
        1. NETWORK_ACTION - create
        1. NETWORK_NAME, e.g. DEMONET
        1. GATEWAY_ACTION - create

        If don't want Azure RG to be deleted part of this job, then keep KEEP_RG option checked.
    ![Image](../images/jenkins-pipeline-create-network-gateway.png)

    1. Run Jenkins job again by selecting on the pipeline created in the previous step. Click on "Build with Parameters"
    1. Fill in service and appwan details by selecting the following:
        1. KEEP_RG - not selected
        1. NF Environment, e.g. production
        1. SERVICE_ACTION - create
        1. APPWAN_ACTION - create
        1. GATEWAY_NAME, e.g. AZCPEGWx0xWESTUS (this is created in the previous step automatically)
        1. SERVICE_NAME, e.g. AZCPEGWx0xWESTUS--10.20.10.5--22 (this is created automatically during this step)
        1. SERVICE_IP, e.g. 10.20.10.5
        1. SERVICE_PORT, e.g. 22
        1. APPWAN_NAME, e.g. appwan-ssh-22
        1. APPWAN_PRIVATE_GATEWAY, e.g.
        1. APPWAN_PRIVATE_CLIENT, e.g.
        1. APPWAN_SERVICE, e.g. AZCPEGWx0xWESTUS--10.20.10.5--22

    ![Image](../images/jenkins-pipeline-create-service-appwan.png)

    To delete the resources created in the previous steps.

    1. Run Jenkins job again by selecting on the pipeline created in the previous step. Click on "Build with Parameters"
    1. Fill in the Azure Details and select the following:
        1. NF Environment, e.g. production
        1. NETWORK_ACTION - delete
        1. NETWORK_NAME, e.g. DEMONET
        1. GATEWAY_ACTION - delete

        Pipeline View
    ![Image](../images/jenkins-pipeline-delete-resources.png)

    1. Done
