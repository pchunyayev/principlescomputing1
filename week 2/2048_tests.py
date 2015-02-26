import poc_simpletest

# I assume that move_left() and merge() are already tested 
# and test only the class.
    
def test_class(game_class):
    """
    Test class
    """
    suite = poc_simpletest.TestSuite()
    
    game = game_class(1, 1)
#    suite.run_test(str(game), str([[0]]), "Test string after reset")
#    suite.run_test(game.get_grid_height(), 1, "Test 1a: get_height")
#    suite.run_test(game.get_grid_width(), 1, "Test 1b: get_width")

    game = game_class(2, 2)
#    #suite.run_test(str(game), str([[0, 0],[0, 0]]), "Test string after reset")
#    suite.run_test(game.get_grid_height(), 2, "Test 1a: get_height")
#    suite.run_test(game.get_grid_width(), 2, "Test 1b: get_width")
#    suite.run_test(game.get_initial_tiles(1), [(0,0),(0,1)], "Up")
#    suite.run_test(game.get_initial_tiles(2), [(1,0),(1,1)], "Down")
#    suite.run_test(game.get_initial_tiles(3), [(0,0),(1,0)], "Left")
#    suite.run_test(game.get_initial_tiles(4), [(0,1),(1,1)], "Right")
   
    game = game_class(2, 3)
#    suite.run_test(str(game), str([[0, 0, 0],[0, 0, 0]]), "Test string after reset")
#    suite.run_test(game.get_grid_height(), 2, "Test get_height")
#    suite.run_test(game.get_grid_width(), 3, "Test get_width")
#    suite.run_test(game.get_initial_tiles(1), [(0,0),(0,1),(0,2)], "Up")
#    suite.run_test(game.get_initial_tiles(2), [(1,0),(1,1),(1,2)], "Down")
#    suite.run_test(game.get_initial_tiles(3), [(0,0),(1,0)], "Left")
#    suite.run_test(game.get_initial_tiles(4), [(0,2),(1,2)], "Right")
      
    game = game_class(5, 2)
#    suite.run_test(str(game), str([[0, 0],[0, 0], [0, 0], 
#                               [0, 0], [0, 0]]), "Test string after reset")
#    suite.run_test(game.get_grid_height(), 5, "Test 1a: get_height")
#    suite.run_test(game.get_grid_width(), 2, "Test 1b: get_width")
#    suite.run_test(game.get_initial_tiles(1), [(0,0),(0,1)], "Up")
#    suite.run_test(game.get_initial_tiles(2), [(4,0),(4,1)], "Down")
#    suite.run_test(game.get_initial_tiles(3), [(0,0),(1,0),(2,0),(3,0),(4,0)], "Left")
#    suite.run_test(game.get_initial_tiles(4), [(0,1),(1,1),(2,1),(3,1),(4,1)], "Right")   

    game = game_class(4, 4)
#    suite.run_test(game.get_initial_tiles(1), [(0,0),(0,1),(0,2),(0,3)], "Up")
#    suite.run_test(game.get_initial_tiles(2), [(3,0),(3,1),(3,2),(3,3)], "Down")
#    suite.run_test(game.get_initial_tiles(3), [(0,0),(1,0),(2,0),(3,0)], "Left")
#    suite.run_test(game.get_initial_tiles(4), [(0,3),(1,3),(2,3),(3,3)], "Right")
   
    
    suite.report_results()