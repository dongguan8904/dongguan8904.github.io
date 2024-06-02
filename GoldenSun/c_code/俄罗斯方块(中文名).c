#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <ncurses.h>

#define 行数 20
#define 列数 15
#define 真 1
#define 假 0

char 游戏区域[行数][列数] = {0};
int 分数 = 0;
char 游戏进行中 = 真;
suseconds_t 方块下落间隔 = 400000;
int 减少 = 1000;

typedef struct {
    char **数组;
    int 宽度, 行, 列;
} 方块;

方块 当前方块;

const 方块 方块数组[7]= {
    {(char *[]){{0,1,1},{1,1,0},{0,0,0}}, 3},
    {(char *[]){{1,1,0},{0,1,1},{0,0,0}}, 3},
    {(char *[]){{0,1,0},{1,1,1},{0,0,0}}, 3},
    {(char *[]){{0,0,1},{1,1,1},{0,0,0}}, 3},
    {(char *[]){{1,0,0},{1,1,1},{0,0,0}}, 3},
    {(char *[]){{1,1},{1,1}}, 2},
    {(char *[]){{0,0,0,0},{1,1,1,1},{0,0,0,0},{0,0,0,0}}, 4}
};

方块 复制方块(方块 方块){
    方块 新方块 = 方块;
    char **复制方块 = 方块.数组;
    新方块.数组 = (char**)malloc(新方块.宽度*sizeof(char*));
    int i, j;
    for(i = 0; i < 新方块.宽度; i++){
        新方块.数组[i] = (char*)malloc(新方块.宽度*sizeof(char));
        for(j=0; j < 新方块.宽度; j++) {
            新方块.数组[i][j] = 复制方块[i][j];
        }
    }
    return 新方块;
}

void 删除方块(方块 方块){
    int i;
    for(i = 0; i < 方块.宽度; i++){
        free(方块.数组[i]);
    }
    free(方块.数组);
}

int 检查方块位置(方块 方块){
    char **数组 = 方块.数组;
    int i, j;
    for(i = 0; i < 方块.宽度;i++) {
        for(j = 0; j < 方块.宽度 ;j++){
            if((方块.列+j < 0 || 方块.列+j >= 列数 || 方块.行+i >= 行数)){
                if(数组[i][j])
                    return 假;
            } else if(游戏区域[方块.行+i][方块.列+j] && 数组[i][j])
                return 假;
        }
    }
    return 真;
}

void 生成并设置新方块(){
    方块 新方块 = 复制方块(方块数组[rand()%7]);
    新方块.列 = rand()%(列数-新方块.宽度+1);
    新方块.行 = 0;
    删除方块(当前方块);
    当前方块 = 新方块;
    if(!检查方块位置(当前方块)){
        游戏进行中 = 假;
    }
}

void 旋转方块(方块 方块){
    方块 临时 = 复制方块(方块);
    int i, j, k, 宽度;
    宽度 = 方块.宽度;
    for(i = 0; i < 宽度 ; i++){
        for(j = 0, k = 宽度-1; j < 宽度 ; j++, k--){
            方块.数组[i][j] = 临时.数组[k][i];
        }
    }
    删除方块(临时);
}

void 更新游戏区域(){
    int i, j;
    for(i = 0; i < 当前方块.宽度 ;i++){
        for(j = 0; j < 当前方块.宽度 ; j++){
            if(当前方块.数组[i][j])
                游戏区域[当前方块.行+i][当前方块.列+j] = 当前方块.数组[i][j];
        }
    }
}

void 清除满行并更新得分(){
    int i, j, 总和, 计数=0;
    for(i=0;i<行数;i++){
        总和 = 0;
        for(j=0;j< 列数;j++) {
            总和+=游戏区域[i][j];
        }
        if(总和==列数){
            计数++;
            int l, k;
            for(k = i;k >=1;k--)
                for(l=0;l<列数;l++)
                    游戏区域[k][l]=游戏区域[k-1][l];
            for(l=0;l<列数;l++)
                游戏区域[k][l]=0;
            方块下落间隔-=减少--;
        }
    }
    分数 += 100*计数;
}

void 打印游戏区域(){
    char 缓冲[行数][列数] = {0};
    int i, j;
    for(i = 0; i < 当前方块.宽度 ;i++){
        for(j = 0; j < 当前方块.宽度 ; j++){
            if(当前方块.数组[i][j])
                缓冲[当前方块.行+i][当前方块.列+j] = 当前方块.数组[i][j];
        }
    }
    clear();
    for(i=0; i<列数-9; i++)
        printw(" ");
    printw("俄罗斯方块\n");
    for(i = 0; i < 行数 ;i++){
        for(j = 0; j < 列数 ; j++){
            printw("%c ", (游戏区域[i][j] + 缓冲[i][j])? '#': '.');
        }
        printw("\n");
    }
    printw("\n分数: %d\n", 分数);
}

void 当前玩家输入(int 玩家输入) {
    方块 临时 = 复制方块(当前方块);
    switch (玩家输入) {
        case 's':
            临时.行++;
            if (检查方块位置(临时))
                当前方块.行++;
            else {
                更新游戏区域();
                清除满行并更新得分();
                生成并设置新方块();
            }
            break;
        case 'd':
            临时.列++;
            if (检查方块位置(临时))
                当前方块.列++;
            break;
        case 'a':
            临时.列--;
            if (检查方块位置(临时))
                当前方块.列--;
            break;
        case 'w':
            旋转方块(临时);
            if (检查方块位置(临时))
                旋转方块(当前方块);
            break;
    }
    删除方块(临时);
    打印游戏区域();
}

struct timeval 之前, 现在;

int 需要更新() {
    return ((suseconds_t)(现在.tv_sec * 1000000 + 现在.tv_usec) - ((suseconds_t)之前.tv_sec * 1000000 + 之前.tv_usec)) > 方块下落间隔;
}

int 主函数() {
    srand(time(0));
    分数 = 0;
    int c;
    initscr();
    gettimeofday(&之前, NULL);
    timeout(1);
    生成并设置新方块();
    打印游戏区域();
    while (游戏进行中) {
        if ((c = getch()) != ERR) {
            当前玩家输入(c);
        }
        gettimeofday(&现在, NULL);
        if (需要更新()) {
            当前玩家输入('s');
            gettimeofday(&之前, NULL);
        }
    }
    删除方块(当前方块);
    endwin();
    int i, j;
    for (i = 0; i < 行数; i++) {
        for (j = 0; j < 列数; j++) {
            printf("%c ", 游戏区域[i][j] ? '#' : '.');
        }
        printf("\n");
    }
    printf("\n游戏结束！\n");
    printf("\n分数: %d\n", 分数);
    return 0;
}

/*
{
    'ROWS': '行数',
    'COLS': '列数',
    'TRUE': '真',
    'FALSE': '假',
    'Table': '游戏区域',
    'score': '分数',
    'GameOn': '游戏进行中',
    'timer': '方块下落间隔',
    'decrease': '减少',
    'Shape': '方块',
    'array': '数组',
    'width': '宽度',
    'row': '行',
    'col': '列',
    'ShapesArray': '方块数组',
    'CopyShape': '复制方块',
    'DeleteShape': '删除方块',
    'CheckPosition': '检查方块位置',
    'SetNewRandomShape': '生成并设置新方块',
    'RotateShape': '旋转方块',
    'WriteToTable': '更新游戏区域',
    'RemoveFullRowsAndUpdateScore': '清除满行并更新得分',
    'PrintTable': '打印游戏区域',
    'ManipulateCurrent': '当前玩家输入',
    'before_now': '之前',
    'now': '现在',
    'hasToUpdate': '需要更新',
    'main': '主函数'
}
*/