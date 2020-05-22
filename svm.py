import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm


def main():
    # split plain
    print('SVM')
    # points
    X = np.array([[0, 0], [2, 2], [3, 0], [2, 0]])
    # points label
    y = np.array([[-1], [-1], [1], [1]])
    # hyperplan  vector
    w = np.array([1.2, -3.2])
    # offset
    b = -0.5
    # plain axis limits
    x_min, x_max, y_min, y_max = -5, 5, -5, 5
    limits = np.array([x_min, x_max, y_min, y_max])
    print('X shape:', X.shape)
    print('y shape:', y.shape)

    print('w: ', w)
    print('b: ', b)

    plt.figure()
    plt.subplot(121)
    for ind in range(y.shape[0]):
        if y[ind, 0] >= 0:
            plt.plot(X[ind, 0], X[ind, 1], 'or')
        elif y[ind, 0] < 0:
            plt.plot(X[ind, 0], X[ind, 1], 'ob')

    # form y=a*x+cte must find a and cte, from  w.'* pts_x_y + b;
    pts_x = np.array([[x_min], [x_max]])
    a = w[0] / w[1]
    cte = b / w[1]
    pts_y = -a * pts_x - cte
    # plot plain
    plt.plot(pts_x, pts_y, '-g')

    # hyperplan parameters
    hyperplan = np.transpose(y) * (w @ np.transpose(X) + b)
    # functional marge rho we take the minimal value of the
    rho = np.min(hyperplan)
    print('functional marge \n rho = ', rho)

    # change parameters of w and b divded by rho in order to have y.' .* (w.'* X.' + b) = 1
    w = w / rho
    b = b / rho
    # verification
    hyperplan_ver = np.transpose(y) * (w @ np.transpose(X) + b)
    rho_ver = np.min(hyperplan_ver)
    print('verifycation that y*(w*X+b)=1 once divided by \n rho = ', rho_ver)
    if rho_ver == 1:
        print('Same Hyperplan')
    else:
        print('Not same plan')

    print('w: ', w)
    print('b: ', b)

    pts_x = np.array([[x_min], [x_max]])
    a = w[0] / w[1]
    cte = b / w[1]
    pts_y = -a * pts_x - cte

    plt.plot(pts_x, pts_y, '*c')


if __name__ == '__main__':
    main()
