from libs import *

class DeleteStreamTest(unittest.TestCase):
    __client = ClientAPI();

    def test_delete_stream(self):
        streamId = "DeleteStreamTest_test_delete_stream_stream_id"
        try:
            self.__client.CreateStream(streamId,"")
            self.__client.DeleteStream(streamId,1)
            self.assertTrue(True)
        except:
            self.assertTrue(False)
