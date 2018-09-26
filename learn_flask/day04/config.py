class Config:
    DEBUG = None
    SECRET_KEY = 'KunQxCm1iQ8ixXGeT9muXbxQyczO8ij2DC4RZBse6hXpLBD07FpbX2RuzrtaniZnUX8'

# 开发模式
class DevelopmentConfig(Config):
    DEBUG = True

# 生产模式
class ProductionConfig(Config):
    DEBUG = False

# 定义配置字典映射
config_dict = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}

