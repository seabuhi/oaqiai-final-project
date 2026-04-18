import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit tests for emotion_detector function."""

    def test_joy(self):
        """Test joy detection."""
        result = emotion_detector('I love this!')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """Test anger detection."""
        result = emotion_detector('I am so angry!')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """Test disgust detection."""
        result = emotion_detector('I hate this!')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """Test sadness detection."""
        result = emotion_detector('I am so sad about this.')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """Test fear detection."""
        result = emotion_detector('I am so scared!')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()