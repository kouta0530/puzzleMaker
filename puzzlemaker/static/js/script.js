var puzzle;
var puzzlePannels = [];

$(".puzzle").on("mousedown",function(){
    
    puzzle = $(this);

    puzzle.css("position","absolute");
    $(document).on("mousemove",onMouseMove);
});

/*
window.onbeforeunload = (e)=>{
    return "パズルを保存しますか？";
}
*/

function onMouseMove(event){
    var x = event.pageX;
    var y = event.pageY;
    var width = x - (puzzle.outerWidth() /2);
    var height =y - (puzzle.outerHeight() /2);
    

    puzzle.css("top",height +"px");
    puzzle.css("left",width +"px");

    $(document).on("mouseup",pannelTouchpieceJudge);
    $(document).on("mouseup",mouseUp);
}

function mouseUp(event){
    $(document).off("mousemove",onMouseMove);
    $(document).off("mouseup",mouseUp);
}


function pannelTouchpieceJudge(){
    var pannel = $(".pannelFrame").find("#" + Number(puzzle.attr("id")));
    
    var pzp = puzzle.position();
    var pnp = pannel.position();

    pnp.top = Math.ceil(pnp.top);
    pnp.left = Math.ceil(pnp.left);
    
    var judgeTop = (pnp.top - 10 < pzp.top)  & (pzp.top < pnp.top + 10);
    var judgeLeft = (pnp.left -10  < pzp.left) & (pzp.left < pnp.left + 10); 

    if(judgeTop & judgeLeft){
        pannel.css("background-image","url("+ puzzle.attr("src") + ")");
        puzzle.remove();
        
        const pId  = Number(puzzle.attr("id")) || 0 ;
        puzzlePannels[pId] = 1;
        console.log(puzzlePannels,pId);
        checkRemainder();

    }

    $(document).off("mouseup",pannelTouchpieceJudge);
}

function checkRemainder(){
    var remainder = $(".remainder");
    remainder.text(remainder.text() - 1);
}
