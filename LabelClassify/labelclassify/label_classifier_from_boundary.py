from label_classifier import LabelClassifier

class LabelClassifierFromBoundary(LabelClassifier):
    def __init__(self, datetime):
        super().__init__(datetime)
    
    @staticmethod
    def fromStringFormat(strf):
        try:
            time = datetime.strptime(strf, "%Y:%m:%d %H:%M:%S")
            return LabelClassifierFromBoundary(time)
        except ValueError as e:
            print(e, file=sys.stderr)