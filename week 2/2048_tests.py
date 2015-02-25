import poc_simpletest

# I assume that move_left() and merge() are already tested 
# and test only the class.
    
def test_class(game_class):
    """
    Test class
    """
    suite = poc_simpletest.TestSuite()
    
    game = game_class(1, 1)
    #suite.run_test(str(game), str([[0]]), "Test string after reset")
    suite.run_test(game.get_grid_height(), 1, "Test 1a: get_height")
    suite.run_test(game.get_grid_width(), 1, "Test 1b: get_width")

    game = game_class(2, 2)
    #suite.run_test(str(game), str([[0, 0],[0, 0]]), "Test string after reset")
    suite.run_test(game.get_grid_height(), 2, "Test 1a: get_height")
    suite.run_test(game.get_grid_width(), 2, "Test 1b: get_width")
    
    game = game_class(2, 3)
    #suite.run_test(str(game), str([[0, 0, 0],[0, 0, 0]]), "Test string after reset")
    suite.run_test(game.get_grid_height(), 2, "Test get_height")
    suite.run_test(game.get_grid_width(), 3, "Test get_width")
    
    game = game_class(5, 2)
    #suite.run_test(str(game), str([[0, 0],[0, 0], [0, 0], 
    #                           [0, 0], [0, 0]]), "Test string after reset")
    suite.run_test(game.get_grid_height(), 5, "Test 1a: get_height")
    suite.run_test(game.get_grid_width(), 2, "Test 1b: get_width")
    
    
    suite.report_results()