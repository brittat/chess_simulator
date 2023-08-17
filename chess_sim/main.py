import argparse
import chess
import chess.svg

class Chess:
    def __init__(self):
        self.board = chess.Board()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
    prog='ChessSimulator',
    description='Accepts a list of uci compliant chess moves and writes the resulting board state to an svg file',
    epilog='Text at the bottom of help')
    parser.add_argument('-np', '--no-print', help='Supress printing the board state')
#    parser.add_argument('board_svg_filename', required=False, help='File name for resulting state, defaults to chess_sim_{git HEAD short hash}')           
    parser.add_argument('-ms', '--moves', type=str, nargs='+', help='Chess moves')
    args = parser.parse_args()
    print(args.moves)
