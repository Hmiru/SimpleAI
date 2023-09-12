from datarecord.data_recorder_from_dir_with_id import DataRecorderFromDirWithID
import yaml
import shutil

class DirectoryRecorderFromDirWithID(DataRecorderFromDirWithID):
    def __init__(self, id: int):
        super().__init__(id)
        self.__image_dir = None
        self.__get_image_dir()

    def __get_image_dir(self):
        with open(os.path.dirname(__file__) + '/../propertise.yaml') as f:
            propertise = yaml.full_load(f)
            self.__image_dir = propertise['location']["Image"]

    def record(self):
        self.to_label_dir()

    def to_label_dir(self):
        source = self.image_location()
        destination_parent = self.__image_dir + "/" + \
                      self.label() + "/" 
        destination = destination_parent + str(self.id()) + ".jpg"

        self.__make_dir_if_not_exists(destination_parent)
        
        shutil.move(source, destination)

        print("Moved image from {} to {}".format(source, destination))

    @staticmethod
    def __make_dir_if_not_exists(path):
        if (not(os.path.exists(path))):
            os.mkdir(path)
        

def main():
    print("No main")

if __name__ == "__main__":
    main()