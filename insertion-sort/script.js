function insertionSort(array){
    const arr = [...array];

    for(let i=1; i<array.length; i++){
        let current = arr[i];
        let j=i-1;

        while (j>=0 && arr[j]>current){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=current;
    }
    return arr;
}