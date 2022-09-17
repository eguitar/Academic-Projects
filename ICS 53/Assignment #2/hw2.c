// Brennen Wong, netID: brennew, #63218897
// Eric Trinh, netID edtrinh, #20091235

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <ctype.h>
#include <signal.h>
#include <fcntl.h>

struct Process
{
    int ground;   // 1:foreground | 0:background | -1:empty
    int jid;
    pid_t pid;
    int state;    // 1:running | 0:stopped
    char command[80];
};

int job_count = 0;
int job_ids = 1;
struct Process jobs[] = {
	{.ground = -1, .jid = 0, .pid = 0, .state = -1, .command = ""},
	{.ground = -1, .jid = 0, .pid = 0, .state = -1, .command = ""},
	{.ground = -1, .jid = 0, .pid = 0, .state = -1, .command = ""},
	{.ground = -1, .jid = 0, .pid = 0, .state = -1, .command = ""},
	{.ground = -1, .jid = 0, .pid = 0, .state = -1, .command = ""}
    };

void command_parse(char* string, char** argv);

int contains_amp(char** argv);

int contains_mod(char* string);

int contains_read(char** argv);

int contains_write(char** argv);

int contains_append(char** argv);

void add_job(int index,int ground,pid_t pid,int state,char* cmdline);

void del_job(pid_t pid);

pid_t get_pid(char* string);

int get_empty_index();

int get_job_index(pid_t pid);

int get_fore_index();

void c_handler(int sig);

void z_handler(int sig);

void chld_handler(int sig);


// --------------------------------------------------------------------------------------------------
int main()
{
    int MaxLine = 80;
	int MaxArgc = 80;
	int MaxJob = 5;
	char cmdline[MaxLine];           // user input commandline
	char cmdline_copy[MaxLine];      // user input commandline copy
	char* argv[MaxArgc];             // argument vector for commands
    char* argv_copy[MaxArgc];        // argument vector for commands copy
    
	extern struct Process jobs[];
    extern int job_count;
    extern int job_ids;

	int inFileID;
    int outFileID;
    char* input_file;
    char* output_file;
    char buffer[MaxLine];
    int op_index;
    mode_t mode = S_IRWXU | S_IRWXG | S_IRWXO;

    while (1)
    {
		signal(SIGINT, c_handler);
		signal(SIGTSTP, z_handler);
		signal(SIGCHLD, chld_handler);
        
        int status;
        printf("prompt> ");
		fgets(cmdline, MaxLine, stdin);      // cmd input
        strcpy(cmdline_copy,cmdline);        // copy of cmd input
		command_parse(cmdline,argv);
        
        if (strcmp(argv[0],"quit") == 0)           // quit
        {
            exit(0);
        }
        else if (strcmp(argv[0],"jobs") == 0)      // jobs
        {
            int i;
            for (i = 0; i < job_count; ++i)
            {
                if (jobs[i].ground == 0)
                {
                    printf("[%d]\t(%d)\t", jobs[i].jid, jobs[i].pid);
                    if (jobs[i].state == 0)
                        printf("Stopped\t");
                    else
                        printf("Running\t");
                    printf("%s",jobs[i].command);
                }
            }
        }
        else if (strcmp(argv[0],"bg") == 0)
        {
            int pid = get_pid(argv[1]);
            int index = get_job_index(pid);
            if (jobs[index].state == 0)
            {
                jobs[index].state = 1;
                kill(pid,SIGCONT);
            }
        }
        else if (strcmp(argv[0],"fg") == 0)
        {
            int pid = get_pid(argv[1]);
            int index = get_job_index(pid);
            jobs[index].ground = 1;
            if (jobs[index].state == 0)
            {
                jobs[index].state = 1;
                kill(pid,SIGCONT);
            }
            pause();
        }
        else if (strcmp(argv[0],"kill") == 0)     // kill
        {
            int pid = get_pid(argv[1]);
            int index = get_job_index(pid);
            if (jobs[index].state == 0)
                kill(pid,SIGCONT);
            kill(pid,SIGINT);
            del_job(pid);
        }
        else if (strcmp(argv[0],"cd") == 0)       // cd    
        {
            chdir(argv[1]);
        }
        else                                      // general commands
        {
            if (contains_amp(argv))               // background
            {
                // printf("background\n");
                pid_t pid = fork();
                setpgid(0,0);
                int index = get_empty_index();
                add_job(index,0,pid,1,cmdline_copy);

                if (jobs[index].pid == 0)
                    if (execv(argv[0], argv) == -1)
                        if (execvp(argv[0], argv) == -1)
                            printf("COMMAND NOT FOUND.\n");
            }
            else                                  // foreground
            {


                pid_t pid = fork();
                setpgid(0,0);
                int index = get_empty_index();
                add_job(index,1,pid,1,cmdline_copy);

            
                
				// we need this here you cant erase it
                
                int read = contains_read(argv);
				int write = contains_write(argv);
				int append = contains_append(argv);


                if (jobs[index].pid == 0)
                {
                    if (read)             // read input from file
					{
                        input_file = argv[read+1];
					    inFileID = open(input_file, O_RDONLY, mode);
                        dup2(inFileID, STDIN_FILENO);
						argv[read] = NULL;
                        close(inFileID);
					}

					if (write)            // write output to file
					{
						output_file = argv[write+1];
						outFileID = open(output_file, O_CREAT|O_WRONLY|O_TRUNC, mode);
						dup2(outFileID, STDOUT_FILENO);
						argv[write] = NULL;
						close(outFileID);
					}
                    else if (append)      // append output to file
                    {
						output_file = argv[append+1];
                        outFileID = open(output_file, O_CREAT|O_WRONLY|O_APPEND, mode); 
                        dup2(outFileID, STDOUT_FILENO);
						argv[append] = NULL;
						close(outFileID);
                    }

                    if (execv(argv[0], argv) == -1)
                        if (execvp(argv[0], argv) == -1)
                            printf("COMMAND NOT FOUND.\n");
                }
                pause();
            }  
        }
    }
    return 0;
}

// --------------------------------------------------------------------------------------------------

int contains_amp(char** argv)
{
    int i = 0;
    while (argv[i] != NULL)
    {
        if (strcmp(argv[i],"&") == 0)
            return 1;
        i++;
    }
    return 0;
}

int contains_mod(char* string)
{
    char* temp = strchr(string, '%');
    if (temp != NULL)
        return 1;
    else
        return 0;
}

int contains_read(char** argv)
{
    int i = 0;
	while (argv[i] != NULL)
	{
		if (strcmp(argv[i],"<") == 0)
		{
			return i;
		}
		i++;
	}
	return 0;
}

int contains_write(char** argv)
{
    int i = 0;
    while (argv[i] != NULL)
    {
        if (strcmp(argv[i],">") == 0)
            return i;
        i++;
    }
    return 0;
}

int contains_append(char** argv)
{
    int i = 0;
    while (argv[i] != NULL)
    {
        if (strcmp(argv[i],">>") == 0)
            return i;
        i++;
    }
    return 0;
}

void command_parse(char* string, char** argv)
{
    const char delim[] = "\t\n ";
    char* token = strtok(string,delim);
    unsigned i = 0;
    while(token != NULL)
    {
        argv[i] = token;
        token = strtok(NULL, delim);
        i++;
    }
	argv[i] = NULL;
}

int get_empty_index()
{
	extern struct Process jobs[];
	int i;
    for (i = 0; i < 5; i++)
		if (jobs[i].ground == -1)
			return i;
	return -1;
}

void add_job(int index, int ground, pid_t pid, int state, char* cmdline)
{
	extern struct Process jobs[];
	extern int job_count;
	extern int job_ids;
	if (job_count < 5)
	{	
		jobs[index].ground = ground;
		jobs[index].jid = job_ids;
		jobs[index].pid = pid;
		jobs[index].state = state;
		strcpy(jobs[index].command, cmdline);
		job_count++;
		job_ids++;
	}
	else
		printf("Too many jobs");
}

void del_job(pid_t pid)
{
	extern struct Process jobs[];
    extern int job_count;
	int i;
    for (i = 0; i < 5; ++i)
    {
        if (jobs[i].pid == pid)
        {
            jobs[i].ground = -1;
            jobs[i].jid = 0;
            jobs[i].pid = 0;
            jobs[i].state = -1;
            strcpy(jobs[i].command,"");
            job_count--;
            return;
        }
    }
}

pid_t get_pid(char* string)
{
    extern struct Process jobs[];
    if (contains_mod(string))  // for job id
    {
        int jid;
        string++;
        jid = atoi(string);
		int i;
        for (i = 0; i < 5; ++i)
            if (jobs[i].jid == jid)
                return jobs[i].pid;
        return -1;
    }
    else                        // for pid
    {
        return atoi(string);
    }
}

int get_job_index(pid_t pid)
{
    extern struct Process jobs[];
	int i;
    for (i = 0; i < 5; ++i)
            if (jobs[i].pid == pid)
                return i;
    return -1;
}

int get_fore_index()
{
    extern struct Process jobs[];
	int i;
    for (i = 0; i < 5; ++i)
            if (jobs[i].ground == 1)
                return i;
    return -1;
}

void c_handler(int sig)
{
	extern struct Process jobs[];
    printf("%c",'\n');
    int index = get_fore_index();
    if (index != -1)
        kill(jobs[index].pid, SIGINT);
}

void z_handler(int sig)
{
	extern struct Process jobs[];
    printf("%c",'\n');
    int index = get_fore_index();
    if (index != -1)
    {
        kill(jobs[index].pid, SIGSTOP);
        jobs[index].ground = 0;
    }
}

void chld_handler(int sig)
{
    pid_t child_pid;
	int status;

	while ((child_pid = waitpid(-1, &status, WNOHANG|WUNTRACED)) > 0)
	{
		extern int job_count;
		if (WIFSTOPPED(status))        // process is stopped
		{
			int index = get_fore_index();
			jobs[index].state = 0;
		}
        else if (WIFSIGNALED(status) || WIFEXITED(status))	// process needs to be deleted
			del_job(child_pid);
        else
			printf("WAITPID ERROR");
    }
}