%% Week 4 - Function Test
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% Place all functions assigned as coding assignments in the folder which
% contains this file.  Run this script, and check if your functions have
% passed by reading the command window output.
% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%% Clean up workspace and command window
clear variables;
clc;

%% List student IDs
% IDs of students in this class
classIDS={'74964706';'14045380';'17861677';'78018124';'21437882';'17716675';'78452388';'92536673';'25562871';'49297006';'78069384';'89671393';'53538689';'17177868';'53364275';'23163870';'76402986';'35312782';'19621212';'68731886';'51329186';'18109034';'15025642';'16924519';'14452153';'83049912';'20091235';'91395650';'44832607';'22743882';'54924118';'18268141';'65379058';'61932345'};

%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% CHANGE THIS EVERY WEEK
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fncs={'adaptSimpsonInt','rombergInt'};
firstCodingAssngm = 11;
testOrGrade = 'test';
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
results=zeros(max(size(classIDS)),length(fncs)+1);
for i=1:max(size(results))
    results(i,1)=str2num(string(classIDS(i,1)));
end
directoryContents=dir;
sizeCont = size(dir);%Size of the directory
fprintf('%%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n');
fprintf('Checking file names and student IDs:\n')
fprintf('%%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n');
for i=1:sizeCont(1)
    if ~directoryContents(i).isdir
        % Get student ID
        clear stdID;
        for j=1:length(fncs)
            % If the given file has at least as many characters as the
            % names of functions
            if strlength(directoryContents(i).name)>=min(strlength(fncs))
                if length(directoryContents(i).name)>strlength(fncs(j))+1
                    if strcmp(extractBefore(directoryContents(i).name,strlength(fncs(j))+1),fncs(j))
                        currentFunc = j;
                        stdID=extractAfter(directoryContents(i).name,strlength(fncs(j))+1);
                        stdID=extractBefore(stdID,9);
                        break
                    end
                end
            end
        end
        % If didnt find student ID, continue on to next file.
        if ~exist('stdID','var')
            fprintf(' - %s is named incorrectly or is not a function that is graded.\n',directoryContents(i).name);
            continue
        else
            nameFlag=0;
            % Check if student ID matches
            for j=1:max(size(classIDS))
                if strcmp(stdID,classIDS(j,1))
                    currentStudent=j;
                    nameFlag=1;
                    break
                end
            end
            if ~nameFlag
                fprintf(' - Incorrect Student ID: %s\n',stdID);
                continue
            end
        end
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
% CHANGE THIS EVERY WEEK
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if currentFunc == 1
            if abs(-1.426014810049447-feval(string(append(fncs(currentFunc),'_',stdID)),@(x)(100/(x^2)*sin(10/x)),1,3,10^(-4),10))<10^(-4)
                results(currentStudent,currentFunc+1)=1;
            else
                results(currentStudent,currentFunc+1)=0;
            end
        end
        if currentFunc == 2
            Ans=[...
                    0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000;
                    1.57079633 2.09439511 0.00000000 0.00000000 0.00000000 0.00000000;
                    1.89611890 2.00455976 1.99857073 0.00000000 0.00000000 0.00000000;
                    1.97423160 2.00026917 1.99998313 2.00000555 0.00000000 0.00000000;
                    1.99357034 2.00001659 1.99999975 2.00000001 1.99999999 0.00000000;
                    1.99839336 2.00000103 2.00000000 2.00000000 2.00000000 2.00000000...
                    ];
            if norm(Ans-feval(string(append(fncs(currentFunc),'_',stdID)),@sin,0,pi,6),2)<10^(-4)
                results(currentStudent,currentFunc+1)=1;
            else
                results(currentStudent,currentFunc+1)=0;
            end
        end
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    end
end
fprintf('%%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n');
fprintf('Testing if functions run properly:\n')
fprintf('%%~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n');
if strcmp(testOrGrade,'test')
    if min(results(currentStudent,2:end))
        fprintf(' - All functions passed!\n');
    else
        for i=1:length(fncs)
            if ~results(currentStudent,i+1)
                fprintf(' - %s_%s failed\n',string(fncs(i)),string(classIDS(currentStudent)));
            else
                fprintf(' - %s_%s passed.\n',string(fncs(i)),string(classIDS(currentStudent)));
            end
        end
    end
elseif strcmp(testOrGrade,'grade')

end