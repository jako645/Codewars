#!/bin/bash
calculate_gcd(){
  ! (( $1 % $2 )) && echo $2 || calculate_gcd $2 $(( $1 % $2 ))
}

gcdi() {
  local input_array=($1)
  input_array=(${input_array[@]#-})
  local init=${2#-}

  local gcdi_array=$(calculate_gcd $init $input_array)

  for (( i = 1; i < ${#input_array[@]}; i++ )); do
    gcdi_array=(${gcdi_array[@]} $(calculate_gcd ${gcdi_array[i-1]} ${input_array[i]}))
  done

  echo ${gcdi_array[@]}
}

lcmu() {
  local input_array=($1)
  input_array=(${input_array[@]#-})
  local init=${2#-}

  local gcd=$(calculate_gcd $init $input_array)
  local lcmu_array=$(( (init * input_array[0]) / gcd ))

  for (( i = 1; i < ${#input_array[@]}; i++ )); do
    gcd=$(calculate_gcd ${lcmu_array[i-1]} ${input_array[i]})
    local new_lcmu=$(( (lcmu_array[i-1] * input_array[i]) / gcd ))
    lcmu_array=(${lcmu_array[@]} $new_lcmu)
  done

  echo ${lcmu_array[@]}
}

som() {
  local input_array=($1)
  local init=$2

  local som_array=$((init + input_array))

  for (( i = 1; i < ${#input_array[@]}; i++ )); do
    som_array=(${som_array[@]} $(( som_array[i-1] + input_array[i] )))
  done

  echo ${som_array[@]}
}

maxi() {
  local input_array=($1)
  local init=$2

  (( init > input_array[0] )) \
    && local maxi_array=$init \
    || local maxi_array=$input_array

  for (( i = 1; i < ${#input_array[@]}; i++ )); do
    (( maxi_array[i-1] > input_array[i] )) \
      && maxi_array=(${maxi_array[@]} ${maxi_array[i-1]}) \
      || maxi_array=(${maxi_array[@]} ${input_array[i]})
  done

  echo ${maxi_array[@]}
}

mini() {
  local input_array=($1)
  local init=$2

  (( init < input_array[0] )) \
    && local mini_array=$init \
    || local mini_array=$input_array

  for (( i = 1; i < ${#input_array[@]}; i++ )); do
    (( mini_array[i-1] < input_array[i] )) \
      && mini_array=(${mini_array[@]} ${mini_array[i-1]}) \
      || mini_array=(${mini_array[@]} ${input_array[i]})
  done

  echo ${mini_array[@]}
}

operArray() {
  $1 "$2" $3
}


operArray $1 "$2" $3
