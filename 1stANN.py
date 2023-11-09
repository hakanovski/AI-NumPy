import numpy as np

# Sigmoid fonksiyonu ve türevi
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Yapay sinir ağı sınıfı
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4) # 4 gizli düğüm
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # Hata gradyanı hesaplama
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # Ağırlıkları güncelleme
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, epochs=1000):
        for _ in range(epochs):
            self.feedforward()
            self.backprop()

         # Giriş verileri (X) ve etiketler (y) oluşturma
         X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
         y = np.array([[0],[1],[1],[0]])

        # Yapay sinir ağını başlatma ve eğitme
        nn = NeuralNetwork(X, y)
        nn.train(epochs=1500)

        # Sonuçları gösterme
        print(nn.output)

