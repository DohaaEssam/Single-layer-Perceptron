import numpy as np
import pandas as pd
#import random as r
import matplotlib.pyplot as plt


def Preprocessing():
    # preprocessing of penguins
    Penguins = pd.read_csv("penguins.csv")
    # fill-in null values in gender with female
    # transform string values of gender into numeric
    Penguins["gender"].fillna(value="female", inplace=True)
    Penguins["gender"] = Penguins["gender"].replace(['female', 'male'], [1, 0])
    Train1 = Penguins.copy()
    # Train1 = Train1[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "gender", "body_mass_g"]]
    for column in Train1.columns[1:]:
        Train1[column] = (Train1[column] - Train1[column].min()) / (
                Train1[column].max() - Train1[column].min())

    return Train1


def dataSplit(penguins):
    P_Adelie = penguins[0:50]
    P_Gentoo = penguins[50:100]
    P_Chinstrap = penguins[100:150]

    return (P_Adelie, P_Gentoo, P_Chinstrap)


def classes(class1, class2):
    x = Preprocessing()
    A, G, C = dataSplit(x)
    if (class1 == A["species"][1] and class2 == G["species"][52]) or (
            class1 == G["species"][52] and class2 == A["species"][1]):
        return A, G

    elif (class1 == A["species"][1] and class2 == C["species"][101]) or (
            class1 == C["species"][101] and class2 == A["species"][1]):
        return A, C

    else:
        return C, G


def Signum(x):
    if x >= 0:
        return 1
    else:
        return -1

def training(class1, class2, epochs, f1, f2, error, bias,thres):

    train1 = class1[0:30].sample(frac=1)
    train2 = class2[0:30].sample(frac=1)
    t1 = train1["species"][train1.first_valid_index()]
    t2 = train2["species"][train2.first_valid_index()]
    train1 = train1.replace({'species': t1}, {'species': 1})
    train2 = train2.replace({'species': t2}, {'species': -1})
    Train = train1.append(train2)
    predtrain=train1.append(train2)

    weight = [np.random.uniform(0, 1) for i in range(2 + bias)]
    Train.reset_index(inplace=True)
    for i in range(0, int(epochs)):
        for j in range(0, 60):
            if bias == 1:
                x = np.array([Train[f1][j], Train[f2][j], 1])
            else:
                x = np.array([Train[f1][j], Train[f2][j]])

            y = float((np.dot(x, weight)))
            predtrain["species"][j] = y
            if y != Train["species"][j]:
                loss = float(Train["species"][j]) - y
                weight[0] = weight[0] + float(error) * loss * x[0]
                weight[1] = weight[1] + float(error) * loss * x[1]
                if bias == 1:
                    weight[2] = weight[2] + float(error) * loss * x[2]
        errors1 = 0
        for z in range(0, 60):
            y_predict = float((np.dot(x, weight)))
            predtrain["species"][z] = y_predict
            errors = float(Train["species"][z]) - y_predict
            errors1 += (errors*errors)

        mse = errors1 / 60
        if mse < float(thres):
            break

    acc = testing(class1, class2, weight, bias, f1, f2)


def testing(class1, class2, weight, bias, f1, f2):
    test1 = class1[30:50]
    test2 = class2[30:50]
    t1 = test1["species"][test1.first_valid_index()]
    t2 = test2["species"][test2.first_valid_index()]
    test1 = test1.replace({'species': t1}, {'species': 1})
    test2 = test2.replace({'species': t2}, {'species': -1})

    actual = test1.append(test2)
    actual.reset_index(inplace=True)

    pred = test1.append(test2)
    pred.reset_index(inplace=True)

    correct = 0

    for j in range(0, 40):
        if bias == 1:
            x = np.array([actual[f1][j], actual[f2][j], 1])
        else:
            x = np.array([actual[f1][j], actual[f2][j]])

        yhat = Signum(np.dot(weight, x))
        pred['species'][j] = yhat




        #pred["species"][j] = yhat

        if yhat == actual["species"][j]:
            correct += 1
    #print(pred)
    accuracy = 100 * (correct / 40)
    print("Accuracy: %.2f%%" % accuracy)

    if bias == 1:
        xi = -weight[2] / weight[0]
        xj = -weight[2] / weight[1]
        plt.plot([xi, 0], [0, xj])
    elif bias==0:
        x = np.linspace(actual.loc[:, f1].min(), actual.loc[:, f2].max())
        y = (-(weight[0] * x)) / weight[1]
        plt.plot(x, y, linestyle='solid')


    plt.scatter(test1[f1], test1[f2])
    plt.scatter(test2[f1], test2[f2])
    cm = np.zeros((2, 2))
    # form an empty matric of 2x2
    num_of_samples=40

    for i in range(num_of_samples):
        # the confusion matrix is for 2 classes: 1,0
         #1=positive, 0=negative
        if (actual["species"][i]) == 1 and (pred["species"][i]) == 1:
            cm[0, 0] += 1
        elif (actual["species"][i]) == 1 and (pred["species"][i]) == -1:
            cm[0, 1] += 1
        elif (actual["species"][i]) == -1 and (pred["species"][i]) == 1:
            cm[1, 0] += 1
        elif (actual["species"][i]) == -1 and (pred["species"][i]) == -1:
            cm[1, 1] += 1
    cm1=dict(enumerate(cm))
    cm1={'true postive':cm[0,0],
         'false positive':cm[0,1],
         'false negative':cm[1,0],
         'true negative':cm[1,1]}
    print(cm1)


    plt.show()



    return accuracy