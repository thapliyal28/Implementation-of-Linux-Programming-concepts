#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>//for pipe
#include<sys/types.h>
#include<sys/wait.h>
#include<errno.h>
#include<string.h>

int main(int argc, char *argv[]){

	int pfd_rgen_a1[2];//0 stdin,1 stdout
	int pfd_a1_a2[2];
	char s[5000];
	if(pipe(pfd_rgen_a1)== -1){
		perror("pipe_rgen_a1");
		exit(1);
	}
	if(pipe(pfd_a1_a2)== -1){
		perror("pipe_a1_a2");
		exit(1);
	}

    pid_t a3_rgen=fork();// returns rgen pid
    
   	if(a3_rgen == 0)
	{
		close(pfd_rgen_a1[0]);//close read end of a pipe
		dup2(pfd_rgen_a1[1],STDOUT_FILENO);//connect standard output i.e stdout of a rgen with the file descripter write of a pipe
		execvp("./rgen", argv);
    }else{
		pid_t a3_a1= fork();// returns a1 pid
		
		if(a3_a1 == 0){
			close(pfd_rgen_a1[1]);//close write end of a pipe
			dup2(pfd_rgen_a1[0],STDIN_FILENO);//connect standard input i.e stdin of a1 with read end of a file.

			close(pfd_a1_a2[0]);//close read end of pipe b/w a1 and a2.
			dup2(pfd_a1_a2[1],STDOUT_FILENO);//now connect standard output i.e stdout of a1 with write part of 2 pipe

			execl("/usr/bin/python", "/usr/bin/python", "./ece650-a1.py", (char *)NULL);
		}else{
			pid_t a3_a2= fork();//  returns a2 pid
			
			if(a3_a2 == 0){
				close(pfd_a1_a2[1]);
				dup2(pfd_a1_a2[0],STDIN_FILENO);
				execvp("./ece650-a2",NULL);
				
			}
		}
	}


	while(fgets(s,5000,stdin)){
		write(pfd_a1_a2[1],s,strlen(s));
	}

	
	
	
	kill(a3_rgen,SIGKILL);
	//kill(getpid(),SIGINT);
	
	return 0;
}


