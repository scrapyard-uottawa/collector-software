import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage


class firebaseClient:

    def __init__(self, machine_id: str):
        """Initialize the firebase client

        Args:
            machine_id (str): the id of the machine
        """
        self.machine_id = machine_id
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred,{'storageBucket': 'scrapyard-7fbdb.appspot.com'})
        db = firestore.client()
        # get the root of the storage bucket
        self.storageBucket = storage.bucket()  # get the storage bucket

        # load the machine data from firebase
        self.dbMachine = db.collection(u'machines').document(self.machine_id)
        self.dbCollection = db.collection(u'machines').document(self.machine_id).collection(u'detections')


    def uploadNewCollectionEvent(self, imagePath:str, machineLearningConfidence, wasteType: str):
        """Upload a new collection event to firebase

        Args:
            machineLearningConfidence (float): the confidence of the machine learning model
            wasteType (str): the type of the waste
        """
        data = {
            u'timeStamp': firestore.SERVER_TIMESTAMP,
            u'capturedImage': u'',
            u'machineLearningConfidence': machineLearningConfidence,
            u'wasteType': wasteType
        }

        doc_ref = self.dbCollection.document()  # get a new document reference
        doc_id = doc_ref.id # get the id of the document
        # get the image from the folder
        image_path = f'{imagePath}'  # get the image path
        # get the extension of the image
        image_extension = image_path.split('.')[-1]  # get the extension of the image

        # upload the image with the format machine_id/doc_id.<extension> to the storage bucket
        blob = self.storageBucket.blob(f'{self.machine_id}/{doc_id}.{image_extension}')  # get the blob
        blob.upload_from_filename(image_path)  # upload the image to the blob
        blob.make_public()  # make the image public
        image_url = blob.public_url  # get the public url of the image
        data[u'capturedImage'] = image_url  # add the image url to the data
        doc_ref.set(data)  # set the data in the document
        print(f'uploaded new collection event to firebase with id {doc_id}')


    def updateBinCapacity(self, binName: str, binCapacity: int):
        """Update the bin capacity of the machine
        
        Args:
            binName (str): the name of the bin
            binCapacity (int): the capacity of the bin
            """
        # get the binCapacity map from the machine document
        binCapacityMap = self.dbMachine.get().to_dict()[u'binCapacity']  # get the binCapacity map from the machine document
        binCapacityMap[binName] = binCapacity  # update the binCapacity map
        self.dbMachine.update({u'binCapacity': binCapacityMap})  # update the machine document


if __name__ == "__main__":
    test = firebaseClient("4HD4nUV5Kkkkt4AUxmSC")
    test.uploadNewCollectionEvent(0.5, "garbage")
    test.updateBinCapacity("garbage", 50)
    print("done") # this is where I get the error




