"""Unit tests for the emotion detector."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests for emotion_detector."""

    def test_emotion_detector(self):
        """Check the dominant emotion for five statements."""
        cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertEqual(result['dominant_emotion'], expected)


if __name__ == '__main__':
    unittest.main()
