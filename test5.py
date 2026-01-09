from sklearn.impute import SimpleImputer

# 1) Drop columns with missing values
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]

reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

score_1 = score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid)


# 2) Imputation
imputer = SimpleImputer(strategy='mean')

imputed_X_train = pd.DataFrame(imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(imputer.transform(X_valid))

imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

score_2 = score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid)


# 3) Imputation + Missing Indicator
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()

for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

imputer = SimpleImputer(strategy='mean')

imputed_X_train_plus = pd.DataFrame(imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(imputer.transform(X_valid_plus))

imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns

score_3 = score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid)


print(score_1)
print(score_2)
print(score_3)
