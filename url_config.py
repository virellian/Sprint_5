class UrlConfig:
    base_url = 'https://stellarburgers.nomoreparties.site/'

    @staticmethod
    def get_full_url(page=''):
        return f'{UrlConfig.base_url}{page}'
