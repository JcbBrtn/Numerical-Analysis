import pandas as pd

class BinReg:
    def __init__(self):
        self.values = []

    def fit(self, X):
        """
        For each point of data in X,
        assuming all values in X are ones in the set we are looking to classify -
        Build a function that uses each point as a root of the function.
        """
        df = pd.DataFrame(X)

        for i in df.iterrows():
            self.values.append(i[1].product())

    def predict(self, X, normalize_out = False):
        predicted_values = []
        df = pd.DataFrame(X)
        print(df)
        for i in df.iterrows():
            prod = i[1].product()
            total = 1
            for val in self.values:
                total = total * (abs(prod - val))
            predicted_values.append(total)

        if normalize_out:
            max_out = max(predicted_values)

            if max_out == 0:
                #All values are already normalized if max output is 0
                return predicted_values

            normalized_predicted_values = []

            for pred in predicted_values:
                normalized_predicted_values.append(pred / max_out)

            return normalized_predicted_values
        
        else:
            return predicted_values

def main():
    model = BinReg()

    X = [[1,4,6,9,1],
         [5,3,2,1,5],
         [3,4,5,6,7],
         [3,5,8,9,1],
         [2,2,8,1,7]]

    model.fit(X)

    X_test = [[5,4,3,2,1],
              [6,7,8,9,1],
              [5,2,4,6,8],
              [7,2,3,1,4],
              [1,4,6,9,1]]

    print(model.predict(X_test, normalize_out=True))

if __name__ == '__main__':
    main()