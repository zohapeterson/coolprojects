#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <string>
#include <time.h>

using namespace std;

void display_field(int grid_array[][6], char show_array[][6], int columns, int rows, int mine_number);
void mine_setup(int grid_array[][6], int mine_number, int columns, int rows);
void randomNUM(int grid_array[][6], int mine_number, int columns, int rows, int& randomINT_1, int& randomINT_2);
void create_numbers(int grid_array[][6], int mine_number, int columns, int rows);
void choose_numbers(int grid_array[][6], char show_array[][6], int columns, int rows, int mine_number, bool& win);
void check_zero(int grid_array[][6], char show_array[][6], int columns, int rows, int input_row, int input_column);

static int x = -1;
static int y = -1;

int main(){
    const int rows = 5, columns = 6, mine_number = 5;
    char show_array[rows][6] = {};
    int grid_array[rows][6] = {};
    ofstream output;
    string user_name;
    double time_elapsed;
    bool win = true;

    output.open("scores.txt", ios::app);
    
    if(output.fail()){
        cout << "FAILED: output file failed to open!" << endl;
        exit(1);
    }
    
    cout << "Welcome to Minesweeper!\nName: ";
    cin >> user_name;
    
    cout << "Symbol meanings:\n* = mine\n- = blank/not revealed\n! = flag\nnumbers = number of mines around that spot\nYour score will be based on time. Good luck!" << endl << endl;
    
    time_t begin, end;
    time(&begin);

    for(int i = 0; i < rows; i++){
        for(int j = 0; j < 6; j++){
            show_array[i][j] = '-';
        }
    }
    
    mine_setup(grid_array, mine_number, columns, rows);
    create_numbers(grid_array, mine_number, columns, rows);
    
    cout << "Mines left: " << mine_number << endl << endl;
    
    display_field(grid_array, show_array, columns, rows, mine_number);
    choose_numbers(grid_array, show_array, columns, rows, mine_number, win);
    
    time(&end);
    time_elapsed = difftime(end, begin);
    
    if(win == true){
        cout << "Your time was " << time_elapsed << " seconds!" << endl;
        output << user_name << ": " << time_elapsed  << " seconds"<< endl;
    } else {
        output << user_name << ": Lost!" << endl;
    }
    
    output.close();
    
    return 0;
}

void display_field(int grid_array[][6], char show_array[][6], int columns, int rows, int mine_number){
    cout << "Column:" << setw(2) << "|";
    for(int u = 0; u < columns; ++u){
        cout << ((u + 1) % 10) << "|";
    }
    cout << endl;
    cout.setf(ios::left);
    cout << setw(9) << " "; 
    cout.unsetf(ios::left);
    cout.setf(ios::right);
    
    for(int t = 0; t < columns; ++t){
        cout << "- ";
    }
    
    cout << endl;
    for(int j = 0; j < rows; j++){
        cout << "Row" << setw(3) << (j + 1)  << ":" << setw(2) << "|";
        for(int z = 0; z < columns; z++){
            cout << show_array[j][z] << "|";
        }
        cout << endl;
        cout.setf(ios::left);
        cout << setw(9) << " "; 
        cout.unsetf(ios::left);
        cout.setf(ios::right);
        
        for(int y = 0; y < columns; y++){
            cout << "- ";
        }
        cout << endl;
    }
}
void mine_setup(int grid_array[][6], int mine_number, int columns, int rows){
    int rand_row = 0, rand_column = 0, randomINT_1 = 0, randomINT_2 = 0;
    
    for(int i = 0; i < mine_number; i++){
        randomNUM(grid_array, mine_number, columns, rows, randomINT_1, randomINT_2); //1, 2
        grid_array[randomINT_1][randomINT_2] = -1;
    }
}
void create_numbers(int grid_array[][6], int mine_number, int columns, int rows){
    int mine_counter = 0;
    
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){

            if((grid_array[i + 1][j + 1] == -1 && grid_array[i][j] != -1) && (i + 1 < rows && j + 1 < columns)){//top right
                mine_counter++;
            } 
            if((grid_array[i - 1][j + 1] == -1 && grid_array[i][j] != -1) && (i - 1 > -1 && j + 1 < columns)){//top left
                mine_counter++;
            } 
            if((grid_array[i + 1][j - 1] == -1 && grid_array[i][j] != -1) && (i + 1 < rows && j - 1 > -1)){//bottom right
                mine_counter++;
            } 
            if((grid_array[i - 1][j - 1] == -1 && grid_array[i][j] != -1) && (i - 1 > -1 && j - 1 > -1)){//top left
                mine_counter++;
            } 
            if((grid_array[i + 1][j] == -1 && grid_array[i][j] != -1) && (i + 1 < rows)){//middle right
                mine_counter++;
            } 
            if((grid_array[i - 1][j] == -1 && grid_array[i][j] != -1) && (i - 1 > -1)){//middle left
                mine_counter++;
            } 
            if((grid_array[i][j + 1] == -1 && grid_array[i][j] != -1) && (j + 1 < columns)){//middle up
                mine_counter++;
            } 
            if((grid_array[i][j - 1] == -1 && grid_array[i][j] != -1) && (j - 1 > -1)){//middle down
                mine_counter++;
            }
            if(grid_array[i][j] == -1){
                mine_counter = -1;

            }
            grid_array[i][j] = mine_counter;
            mine_counter = 0;
        }
    }
}

void randomNUM(int grid_array[][6], int mine_number, int columns, int rows, int& randomINT_1, int& randomINT_2){
    bool repeated = true;
    
    while(repeated == true){
        if(x == 100){
            x = 0;
        }
        if(y == 100){
            y = 0;    
        }
        
        int rands_1[100];
        int rands_2[100];
        srand((unsigned)time(0));
        
        for(int index_1 = 0; index_1 < 100; index_1++){
            rands_1[index_1] = (rand() % rows);
        }
        
        for(int index_2 = 0; index_2 < 100; index_2++){
            rands_2[index_2] = (rand() % columns);
        }
        x++;
        y++;
        
        randomINT_1 = rands_1[x];
        randomINT_2 = rands_2[y];
        
        for(int i = 0; i < mine_number; i++){
            if(grid_array[randomINT_1][randomINT_2] == -1){
                repeated = true;
                break;
            } else {
                repeated = false;
            }
        }
        if(repeated == false){
            break;
        }
    }
}
void choose_numbers(int grid_array[][6], char show_array[][6], int columns, int rows, int mine_number, bool& win){
    int input_row = 0, input_column = 0, temp_num, correct_count = 0, show_mineNumber = mine_number, temp_numCheck;
    char input_flag, temp_char, temp_charCheck;
    bool game_over = false;
    
    cout << "Choose a row and a column to add a flag or to reveal the number of mines surrounding that spot." << endl;
    
    while(game_over == false){
        cout << "Row: ";
        cin >> input_row;
        input_row--;
        while((input_row > (rows - 1) || input_row < 0)){
            cout << "Invalid. Row: ";
            cin >> input_row;
            input_row--;
            
            if(input_row < rows && input_row > 0){
                break;
            }
        }
        
        cout << "Column: ";
        cin >> input_column;
        input_column--;
        while((input_column > (columns - 1) || input_column < 0) || show_array[input_row][input_column] != '-'){
            cout << "Invalid. Column: ";
            cin >> input_column;
            input_column--;
            
            if(input_column < columns && input_column > 0){
                break;
            }
        }
        
        cout << "Flag?(y/n): ";
        cin >> input_flag;
        while(input_flag != 'y' && input_flag != 'n' && input_flag != 'Y' && input_flag != 'N'){
            cout << "Invalid. Flag?(y/n): ";
            cin >> input_flag;
            
            if(input_flag == 'Y' || input_flag == 'N' || input_flag == 'y' || input_flag == 'n'){
                break;
            }
        }
        cout << endl;
        
        if((input_flag == 'n' || input_flag == 'N') && (grid_array[input_row][input_column] != -1)){
            temp_num = grid_array[input_row][input_column] + 48;
            temp_char = (char)temp_num;
            
            show_array[input_row][input_column] = temp_char;
            
            if(grid_array[input_row][input_column] == 0){
                check_zero(grid_array, show_array, columns, rows, input_row, input_column);
            }
            
        } else if((input_flag == 'n' || input_flag == 'N') && (grid_array[input_row][input_column] == -1)){
            game_over = true;
            win = false;
            for(int i = 0; i < rows; i++){
                for(int j = 0; j < columns; j++){
                    if(grid_array[i][j] != -1){
                        temp_num = grid_array[i][j] + 48;
                        temp_char = (char)temp_num;
                        show_array[i][j] = temp_char;
                    } else if(grid_array[i][j] == -1){
                        show_array[i][j] = '*';
                    }
                }
            }
            
        } else if(input_flag == 'y' || input_flag == 'Y'){
            show_array[input_row][input_column] = '!';
            show_mineNumber--;
        }
        
        correct_count = 0;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < 6; j++){
                temp_numCheck = grid_array[i][j] + 48;
                temp_charCheck = (char)temp_numCheck;

                if(show_array[i][j] == '!' && grid_array[i][j] == -1){
                    correct_count++;
                }
                if(show_array[i][j] == temp_charCheck){
                    correct_count++;
                }
            }
        }
        
        cout << "Mines left: " << show_mineNumber << endl << endl;
        
        display_field(grid_array, show_array, columns, rows, mine_number);
        
        if(correct_count == (rows * columns) && win == true){
            win = true;
            cout << "You win!" << endl;
            break;
        }
        
        if(game_over == true){
            cout << "You found a mine. Game over!" << endl << endl;
            break;
        }
    }
}
void check_zero(int grid_array[][6], char show_array[][6], int columns, int rows, int input_row, int input_column){
    int temp_num;
    char temp_char;
    
    if((grid_array[input_row + 1][input_column + 1] == 0 && grid_array[input_row][input_column] == 0) && (input_row + 1 < rows && input_column + 1 < columns)){//top right
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row + 1][input_column + 1] = temp_char;
    } 
    if((grid_array[input_row - 1][input_column + 1] == 0 && grid_array[input_row][input_column] == 0) && (input_row - 1 > -1 && input_column + 1 < columns)){//top left
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row - 1][input_column + 1] = temp_char;
    } 
    if((grid_array[input_row + 1][input_column - 1] == 0 && grid_array[input_row][input_column] == 0) && (input_row + 1 < rows && input_column - 1 > -1)){//bottom right
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row + 1][input_column - 1] = temp_char;
    } 
    if((grid_array[input_row - 1][input_column - 1] == 0 && grid_array[input_row][input_column] == 0) && (input_row - 1 > -1 && input_column - 1 > -1)){//top left
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row - 1][input_column - 1] = temp_char;
    } 
    if((grid_array[input_row + 1][input_column] == 0 && grid_array[input_row][input_column] == 0) && (input_row + 1 < rows)){//middle right
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row + 1][input_column] = temp_char;
    } 
    if((grid_array[input_row - 1][input_column] == 0 && grid_array[input_row][input_column] == 0) && (input_row - 1 > -1)){//middle left
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row - 1][input_column] = temp_char;
    } 
    if((grid_array[input_row][input_column + 1] == 0 && grid_array[input_row][input_column] == 0) && (input_column + 1 < columns)){//middle up
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row][input_column + 1] = temp_char;
    } 
    if((grid_array[input_row][input_column - 1] == 0 && grid_array[input_row][input_column] == 0) && (input_column - 1 > -1)){//middle down
        temp_num = grid_array[input_row][input_column] + 48;
        temp_char = (char)temp_num;
        show_array[input_row][input_column - 1] = temp_char;
    }
}