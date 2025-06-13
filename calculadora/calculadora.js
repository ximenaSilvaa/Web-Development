$(document).ready(function(){
    $("#suma").click(function(){
        let first =  0;
        let second = 0;
        first =$("#fnumber").val();
        second =$("#snumber").val();
        valores = valores = { first: first, second: second };
        $.post("https://ximenasilva.pythonanywhere.com/suma", valores,function(data,status){
            console.log(status)
            $("#result").text(data)
        });
    });

    $("#resta").click(function(){
        let first =  0;
        let second = 0;
        first =$("#fnumber").val();
        second =$("#snumber").val();
        valores = valores = { first: first, second: second };
        $.post("https://ximenasilva.pythonanywhere.com/resta", valores,function(data,status){
            console.log(status)
            $("#result").text(data)
        });
    });

    $("#multiplicacion").click(function(){
        let first =  0;
        let second = 0;
        first =$("#fnumber").val();
        second =$("#snumber").val();
        valores = valores = { first: first, second: second };
        $.post("https://ximenasilva.pythonanywhere.com/multiplicacion", valores,function(data,status){
            console.log(status)
            $("#result").text(data)
        });
    });

    $("#division").click(function(){
        let first =  0;
        let second = 0;
        first =$("#fnumber").val();
        second =$("#snumber").val();
        valores = valores = { first: first, second: second };
        $.post("https://ximenasilva.pythonanywhere.com/division", valores,function(data,status){
            console.log(status)
            $("#result").text(data)
        });
    });
});

