from mkpipe.spark import JdbcLoader


class MysqlLoader(JdbcLoader, variant='mysql'):
    driver_name = 'mysql'
    driver_jdbc = 'com.mysql.cj.jdbc.Driver'

    def build_jdbc_url(self):
        return (
            f'jdbc:{self.driver_name}://{self.host}:{self.port}/{self.database}'
            f'?user={self.username}&password={self.password}'
        )
