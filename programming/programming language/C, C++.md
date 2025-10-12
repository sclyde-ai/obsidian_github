- concept
    - Makefile
        - template
            ```c
            NAME	= object.a
            SRCS	= 
            OBJS	= ${SRCS:%.c=%.o}
            CC = cc
            FLAGS	= -Wall -Wextra -Werror
            $(NAME):
            	$(CC) $(FLAGS) -c $(SRCS) -I ./
            	ar rcs $(NAME) $(OBJS)
            all: $(NAME)
            clean:
            	rm -rf $(OBJS)
            fclean: clean
            	rm -rf $(NAME)
            re: fclean all
            ```
        - &(NAME), all, clean, fclean, reが必要
        - fileは順番に読み込む必要あり
    - operator 演算子
        - sizeof a
        sizeof (type)
            型の大きさを確認
        - (type)
        type(a)
            型をtypeに変換
        - ? 三項演算子 ternary operator
            ```c
            condition ? consequent : alternative
            ```
            ```c
            if (condition) {
                consequemt
            } 
            else {
                alternative
            }
            ```
            上記２つのcodeは等しい
    - dynamic memory allocation
        [<stdlib.h>](https://www.notion.so/stdlib-h-216ec42dd04b81999bd0e9eb48f65a23?pvs=21) 
    - struct 構造体
        - 構造体templete
            ```c
            struct struct_name{
                member1;
                member2;
                ...
            };
            ```
            - 構造体変数の定義
                ```c
                struct struct_name variable;
                ```
        - typedef
            structという文字を省略可能
            ```c
            typedef struct struct_name new_struct_name;
            ```
            - 構造体変数の定義
                ```c
                new_struct_name variable
                ```
        - arrow演算子
            |  | 通常の構造体 | 構造体のpointer |
            | --- | --- | --- |
            | def | struct_name var | struct_name* ptr |
            | member | var.member | ptr->member |
    - variadic argument 可変長引数
        [<stdarg.h>](https://www.notion.so/stdarg-h-216ec42dd04b813fa41add43a97f2743?pvs=21) 
    - static variable 静的変数
        - memoryの割り当てが固定
        - scope内のみアクセス可能だが寿命はprogram全体
        - 宣言時に0で初期化される
    - system
        [<unistd.h>](https://www.notion.so/unistd-h-216ec42dd04b8162a926ed6fc1ed7ef8?pvs=21) 
        - file descriptor
            fileの識別番号
            | 0 | 標準入力 | stdin |
            | --- | --- | --- |
            | 1 | 標準出力 | stdout |
            | 2 | 標準error出力 | stderr |
            | 3以上 | 順番待ち |  |
            - stdin
            - stdout
        - EOF
            end of file 
    - magic number
    - pipe
    - socket
    - stream
    - compile
- c libraries
    - <stdio.h>
        標準入力
        - printf
        - setbuf
        - setvbuf
        - BUFSIZ
            buffer使用時の推奨size
    - <stddef.h>
        typedef
    - <stdint.h>
        整数型
    - <stdlib.h>
        標準library
        - malloc
            heap領域のmemoryの確保
            ```c
            void *malloc(size_t size)
            ```
            - internal behavior
                - memory search
                    free listからmemory blockを検索
                - request new memory
                    free listに解放済みblockが存在しない場合OSに新しいmemoryを要求
                - block splitting
                - metadata
                    確保したblockの前にmetadataを保存
                - 
        - free
            ```c
            void free(void *pointer)
            ```
            pointerはmalloc, calloc, reallocで確保されたmemoryの先頭addressのみ
    - <stdarg.h>
        可変長引数のlibrary 
        - va_list
        - va_start
            ```c
            void va_start(
               va_list arg_ptr,
               prev_param
            );
            ```
        - va_arg
            ```c
            type va_arg(
               va_list arg_ptr,
               type
            );
            ```
        - va_copy
            ```c
            void va_copy(
               va_list dest,
               va_list src
            );
            ```
        - va_end
            ```c
            void va_end(
               va_list arg_ptr
            );
            ```
    - <unistd.h>
        - open
            ```c
            int _open(
               const char *filename,
               int oflag [,
               int pmode]
            );
            ```
            - filename
                開きたいfileのpath
            - oflag
                動作を指定
                | O_RDONLY | 読み取り専用 |
                | --- | --- |
                | O_WRONLY | 書き込み専用 |
                | O_RDWR | 読み書き両用 |
            - pmode (option)
            - return
                | 0 以上 | file descriptor |
                | --- | --- |
                | -1 | error |
            - function
                fileと方法を指定しfile descriptorを返す関数
                1. fileのmeta dataを読み込む
                2. file tableに新しいentryを作成
                3. file descriptorを割り当てる
        - read
            ```c
            int _read(
               int const fd,
               void * const buffer,
               unsigned const buffer_size
            );
            ```
            - fd
                file descriptor
                - fd=1or2にするとerror
            - buffer
                dataの格納場所
            - buffer_size
                読み取り最大byte数
            - return
                bufferに格納した文字数
                | 0 超過 | 読み取りbyte数 |
                | --- | --- |
                | 0 | EOF |
                | -1 | error |
            https://learn.microsoft.com/ja-jp/cpp/c-runtime-library/reference/open-wopen?view=msvc-170
        - write
        - close
            ```c
            int _close(
               int fd
            );
            ```
            - return
                | 0 | 正常 |
                | --- | --- |
                | -1 | error |
        [C Programming/stdlib.h - Wikibooks, open books for an open world](https://en.wikibooks.org/wiki/C_Programming/stdlib.h)
    - <fcntl.h>
        Defines file control options
        - O_RDONLY
        - O_WRONLY
        - O_RDWR
    - <limits.h>
        - LONG_MIN
            -2147483647 - 1
        - LONG_MAX
            2147483647
        - INT_MIN
            2147483647 - 1
        - INT_MAX
            2147483647
        - ULONG_MAX
            4294967295 (0xffffffff)
    - container
- data structure
    - STL container
        - vector
            - O(1)
                - [i]
                - pop_back
                - push_back
        - queue
            - O(1)
                - front
                - pop
                - push
                - empty
        - stack
            - O(1)
                - top
                - pop
                - push
        - deque
            - O(1)
                - front
                - back
                - push_front
                - push_back
                - pop_front
                - pop_back
        - priority_queue
            - O(1)
                - top
            - O(log(n))
                - push
                - pop
        - list
            - O(1)
                - insert
                - erase
        - set
            - O(log(n))
                - insert
                - erase
                - find
            - lower_bond
            - upper_bond
        - map
            - O(log(n))
                - erase
                - find
                - map[x] = value
    - heap
    - union find
    - segment tree
    - BIT binary index tree
- c compiler
    - cc compiler collection
        | -Wall |  |
        | --- | --- |
        | -Werror |  |
        | -Wextra |  |
    - gcc GNU compiler collection
        | -g3 | enable debagging |
        | --- | --- |
        |  |  |
        |  |  |
- error
    - memory
        - gdb GNU debugger
            it is a debugger
            - process
                1. compile
                    ```bash
                    gcc -g3 *.c
                    ```
                2. gdb
                    ```bash
                    gdb a.out
                    ```
                3. breakpoint
                    ```bash
                    b main
                    ```
                4. execution
                    ```bash
                    run
                    ```
            - command
                - b/break
                    - a specific line
                        set a breakpoint at a specific line
                        ```bash
                        break program.c:10
                        ```
                    - a function
                        set a breakpoint at a function
                        ```bash
                        break func
                        ```
                - n/next
                    一回ずつ実行　関数飛ばす
                - s/step
                    一回ずつ実行　関数の中に入る
                - q/quit
                - f
                    関数を抜けるまで実行
                - c
                    次のbreak point まで実行
                - reverse-next
                - reverse-step
            - error
                - Program received signal SIGSEGV, Segmentation fault.
        - valgrind
            | —leak-check=full |  |
            | --- | --- |
            | —track-origin |  |
            | —log-file |  |
            - error
                - Invalid read of size 1
                    - access freed memory
                    - access uninitialized memory
                    - access out-of-range memory
                        - mallocの確保数不足
                    - access NULL pointer
                - 2 bytes in 1 blocks are definitely lost in loss record 1 of 1
                    forgetting free
            - leak summary
                - definitely lost
                - indirectly lost
                - possibly lost
                - still reachable
            [](https://valgrind.org/)
        - segmentation fault (core dumped)
            - NULL pointer
            - freed memory
            - stack overflow
            - out of bounds
            - invalid memory
        - a.out: malloc.c:2617: sysmalloc: Assertion failed
            an internal check in themalloc implementation that has failed. The assertion is verifying that the state of the memory allocator's internal data structures is consistent, and it has detected an inconsistency.
            malloc 関数の内部で、メモリ管理の整合性チェックが失敗したことを示しています。メモリの状態が不正であるため、プログラムが強制終了しました。
        - zsh: IOT instruction (core dumped)
            This indicates that the program crashed and produced a core dump. The "IOT instruction" part suggests that the crash was due to an invalid memory operation.
        - heap領域は絶対にfree
        - mallocしたらNULLかどうかを必ず確認
        - mallocで取得したmemoryは0埋めが望ましい