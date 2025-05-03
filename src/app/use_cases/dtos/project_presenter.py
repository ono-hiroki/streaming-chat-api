# app/use_cases/project_presenter.py
class IndexProjectPresenter:
    def __call__(self, output: dict) -> dict:
        # 必要に応じてレスポンスデータの追加整形
        return output