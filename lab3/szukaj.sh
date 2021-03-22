# #!/bin/bash
# declare -i flag sons
# flag=0
# sons=()

# my_own_find()
# {
#     # if [ -e "$1/$2" ]; then
#     #     echo $1
#     # fi
#     for file in $1/*
#     do
#         if [ -f "$file" ] && [ "$(basename $file)" = "$2" ]; then
#             echo "$1"
#             flag=$((flag+1))
#             sons+=("$!")
#         fi

#         if [ -d "$file" ]; then
#             my_own_find $file $2 &
#             wait $!
#         fi
#     done

#     for son in "${sons[@]}"
#     do
#         wait $!
#     done

#     if [[ -z "$3" ]]; then
#         if [[ $flag -eq 0 ]]; then
#             echo "Nie znaleziono $2"
#         fi
#     fi
    
# }

# my_own_find $1 $2 $3


# # result=$(my_own_find $1 $2)

# # if [[ ! -z "${result// }" ]]; then
# #     echo "$result"
# # else
# #     echo "Nie znaleziono"
# # fi