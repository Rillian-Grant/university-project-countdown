import unittest
import countdown

class TestCountdown(unittest.TestCase):
    def test_letters_to_chose_from(self):
        expected_const_dist = "b b c c c d d d d d d f f g g g h h j k l l l l l m m m m n n n n n n n n p p p p q r r r r r r r r r s s s s s s s s s t t t t t t t t t v w x y z"
        expected_vowel_dist = "a a a a a a a a a a a a a a a e e e e e e e e e e e e e e e e e e e e e i i i i i i i i i i i i i o o o o o o o o o o o o o u u u u u"
        expected_const_dist = expected_const_dist.split(" ")
        expected_vowel_dist = expected_vowel_dist.split(" ")
        
        const_dist, vowel_dist = countdown.letters_to_chose_from()
        
        self.assertEqual(vowel_dist, expected_vowel_dist)
        self.assertEqual(const_dist, expected_const_dist)
    
    def test_word_lookup(self):
        expected_words = "a aa aal ad adad add adda added addle addlehead addleheaded ade adead ado ae ah aha ahead aho al ala alada alala aldehol aldol ale alee all allele allheal alo alod aloe aloed d da dad dada daddle dade dado dae daedal dah dal dale dalle dao de dead deadhead deal dedo dee deed deedeed dele delead dell dha dhole do dod dodd dodded doddle dodo doe dola dole doll dollhood doodad doodle dool doolee e ea eddo edea edh eel eh el eld ell elle elod h ha had haddo hade hah hala halal hale hall hallah hallel halloo halo hao haole he head headed heal heald heddle heed heel heeled hele hell hellhole hello heloe ho hod hoddle hoe hold holdall hole holl holla hollo hood hooded hoodoo l la lad lade ladhood ladle lall lalo lea lead leaded leal led lede ledol lee leed lo loa load loaded lod lode loll loo lood o oadal od oda odal odd ode odel oe oh ohelo oho old oleo olla"
        expected_words = expected_words.split(" ")

        words = countdown.word_lookup("aollhdeoo")

        self.assertEqual(expected_words, words)

if __name__ == "__main__":
    unittest.main()