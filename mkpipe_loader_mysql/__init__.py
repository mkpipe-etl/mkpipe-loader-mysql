from mkpipe.functions_spark import BaseLoader


class MysqlLoader(BaseLoader):
    def __init__(self, config, settings):
        super().__init__(
            config,
            settings,
            driver_name='mysql',
            driver_jdbc='com.mysql.cj.jdbc.Driver',
        )
