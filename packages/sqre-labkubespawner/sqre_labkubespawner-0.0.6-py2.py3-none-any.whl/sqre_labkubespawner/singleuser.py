import os
from .jhubsingleuser import SingleUserNotebookApp
from jupyterlab.labapp import LabApp


class SingleUserLabApp(SingleUserNotebookApp, LabApp):

    def init_webapp(self, *args, **kwargs):
        super(SingleUserLabApp, self).init_webapp(*args, **kwargs)
        settings = self.web_app.settings
        if 'page_config_data' not in settings:
            settings['page_config_data'] = {}
        settings['page_config_data']['hub_prefix'] = self.hub_prefix
        settings['page_config_data']['hub_host'] = self.hub_host
        settings['page_config_data']['hub_user'] = self.user
        token = os.getenv('JUPYTERHUB_API_TOKEN')
        if not token:
            token = ''
        settings['page_config_data']['token'] = token


def main(argv=None):
    return SingleUserLabApp.launch_instance(argv)


if __name__ == "__main__":
    main()
