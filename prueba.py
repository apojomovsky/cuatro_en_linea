from tests.board_builder import BoardBuilder

builder = BoardBuilder('W', 'B')
#board = builder.build_from_moves([1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,3,4,3,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])
#board = builder.build_from_moves([1,4,1,5,1,5,1])
board_test_rows = builder.build_from_moves([1,1,1,2,2,2,3,1,])

print board_test_rows
