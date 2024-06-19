
from matplotlib import pyplot

class Debugger:
    @staticmethod
    def draw_training_history(history):
        pyplot.plot(history['accuracy'], label='Train data')
        pyplot.plot(history['val_accuracy'], label='Valid data')
        pyplot.legend()
        pyplot.show()

    @staticmethod
    def check_test_performance(build_model, test_ds):
        scores = build_model.evaluate(test_ds, batch_size=128, verbose=1)
        print('\nTest result : %.3f loss:%.3f' % (scores[1] * 100, scores[0]))

