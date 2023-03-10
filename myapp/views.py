
from .models import Data
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import pickle
import pandas as pd
from .forms import FeatureForm

# load your pre-trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# load the encoder object
with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)


# define your view function


cat_columns = [
    'Gender', 'Seniorcitizen', 'Partner', 'Phoneservice', 'Multiplelines', 'Internetservice', 'Onlinesecurity', 'Onlinebackup', 'Deviceprotection',
    'Techsupport', 'Streamingtv', 'Streamingmovies', 'Contract', 'Dependents', 'Paymentmethod', 'Paperlessbilling'
]

numerical_cols_for_test = ['Monthlycharges', 'Totalcharges', 'Tenure']

# new_data_points = []
features_col_name_corrected = {}
customer_data = pd.DataFrame()
df = pd.DataFrame()


@csrf_exempt
def feature_taker(request):
    global features_col_name_corrected
    if request.method == 'POST':
        # create a form instance with the POST data
        form = FeatureForm(request.POST)
        columns_labels = [
            form.fields[field_name].label for field_name in form.fields]
        # print(columns_labels)

        # check if the form is valid
        if form.is_valid():
            # get cleaned data from the form
            features = form.cleaned_data
            features_col_name_corrected = {
                columns_labels[i]: features[key] for i, key in enumerate(features)}

            new_data_point = pd.DataFrame.from_dict(
                features, orient='index').T

            # print(new_data_point.columns)
            # new_data_point.columns = new_data_point.columns.str.uppwer()
            # new_data_points.append(new_data_point)

            # print(new_data_point)
            request.session['new_data_point'] = new_data_point.to_dict()

            # return redirect('dataframe_creator')
            return redirect('preprocess_features')
    else:
        form = FeatureForm()
    return render(request, 'user_input.html', {'form': form})


@csrf_exempt
def dataframe_creator(request):
    # global df
    print("dataframe_creator called")
    if request.session.get('new_data_point'):
        df = pd.DataFrame.from_dict(
            request.session['new_data_point'], orient='columns')
        print(df)
        # df = pd.concat(request.session['new_data_points'], ignore_index=True)
    else:
        df = pd.DataFrame()

    return render(request, 'feature_data.html', {'df': df})


# @csrf_exempt
# def dataframe_creator(request):
#     global df
#     print("dataframe_creator called")
#     if new_data_points:
#         df = pd.concat(new_data_points, ignore_index=True)
#     else:
#         df = pd.DataFrame()

#     return render(request, 'feature_data.html', {'df': df})

@csrf_exempt
def preprocess_features(request):
    global customer_data, df
    print("preprocess_features called")
    # print(type(new_data_points))
    if request.session.get('new_data_point'):
        df = pd.DataFrame.from_dict(
            request.session['new_data_point'], orient='columns').reset_index(drop=True)
        # print(f"df is \n {df}")
        new_data_point_cat = df[cat_columns]
        # print(f"new_data_point_cat is \n {new_data_point_cat}")

        # one-hot encode categorical features
        feature_names = encoder.get_feature_names_out(cat_columns)
        # print(feature_names)
        new_data_point_cat_encoded = encoder.transform(new_data_point_cat)

        # combine numerical and encoded features

        num_features = df[numerical_cols_for_test]
        cat_features = pd.DataFrame(
            new_data_point_cat_encoded, columns=feature_names)
        # print(f"df index is \n {df.index}")
        # print(f"num_features index is \n {num_features.index}")
        # print(f"cat_features index is \n {cat_features.index}")

        customer_data = pd.concat([num_features, cat_features], axis=1)

        print(customer_data)
        # df.columns = columns_labels
        df.columns = features_col_name_corrected.keys()
        return redirect('predict')

    else:
        df = pd.DataFrame()
    #
    # return render(request, 'prediction.html', {'prediction': prediction, 'df': df})
    return render(request, 'data_for_ml.html', {'customer_data': customer_data})


# @csrf_exempt
# def preprocess_features(request):
#     global customer_data, df
#     print("preprocess_features called")
#     # print(type(new_data_points))
#     if new_data_points:
#         df = pd.concat(new_data_points, ignore_index=True)
#         new_data_point_cat = df[cat_columns]
#         # one-hot encode categorical features
#         feature_names = encoder.get_feature_names_out(cat_columns)
#         # print(feature_names)
#         new_data_point_cat_encoded = encoder.transform(new_data_point_cat)

#         # combine numerical and encoded features
#         customer_data = pd.concat([df[numerical_cols_for_test], pd.DataFrame(
#             new_data_point_cat_encoded, columns=feature_names)], axis=1)

#         # df.columns = columns_labels
#         df.columns = features_col_name_corrected.keys()
#         return redirect('predict')

#     else:
#         df = pd.DataFrame()
#     #
#     # return render(request, 'prediction.html', {'prediction': prediction, 'df': df})
#     return render(request, 'data_for_ml.html', {'customer_data': customer_data})


@csrf_exempt
def predict(request):

    # make prediction using pre-trained model
    prediction = model.predict_proba(customer_data) * 100
    # print(df.iloc[:, 0:8])
    return render(request, 'prediction.html', {'prediction': prediction, 'df': df})
