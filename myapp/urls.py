from django.urls import path
# from .views import churn_predictor
from . import views

urlpatterns = [
    # path('churn_predictor/', churn_predictor, name='churn_predictor'),
    # path('', views.churn_predictor, name='churn_predictor'),
    path('', views.feature_taker, name='feature_taker'),
    # path('results/', views.dataframe_creator, name='dataframe_creator'),
    path('feature_data/', views.dataframe_creator, name='dataframe_creator'),
    path('preprocess_features/', views.preprocess_features,
         name='preprocess_features'),
    path('predict/', views.predict,
         name='predict'),
    #     path('get_preprocessed_data/', views.get_preprocessed_data,
    #          name='get_preprocessed_data'),

]
