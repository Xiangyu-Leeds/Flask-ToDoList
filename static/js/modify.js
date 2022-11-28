 function member_del(obj, id) {
        layer.confirm('Are you sure you want to delete it permanently? (Non-recoverable)', function (index) {
            //Send asynchronously delete data
            //We'll use async later, but we'll use async here
            $.get("/delete?id=" + id);

            layer.msg('have deleted', {icon: 1, time: 1000});
            setTimeout("location.reload()", "500")
        });
    }

    function member_del1(obj, id) {
        layer.confirm('Are you sure you want to put it in the recycle bin?', function (index) {
             //Send asynchronously delete data
            //We'll use async later, but we'll use async here
            $.get("/delete1?id=" + id);

            layer.msg('Put in the recycle bin!', {icon: 1, time: 1000});
            setTimeout("location.reload()", "500")
        });
    }

    function member_recover(obj, id) {
        layer.confirm('Are you sure you want to recover?', function (index) {
             //Send asynchronously delete data
            //We'll use async later, but we'll use async here
            $.get("/recover?id=" + id);

            layer.msg('have recovered!', {icon: 1, time: 1000});
            setTimeout("location.reload()", "500")
        });
    }

    function cancel(obj, id) {
        layer.confirm('Are you sure you want to cancel', function (index) {
             //Send asynchronously delete data
            //We'll use async later, but we'll use async here
            $.get("/cancel?id=" + id);

            layer.msg('have canceled!', {icon: 1, time: 1000});
            setTimeout("location.reload()", "500")
        });
    }

    function change(obj, id) {
        $.get("/completed_issue?id=" + id);
        setTimeout("location.reload()", "50")


    }

    function change1(obj, id) {
        $.get("/uncompleted_issue?id=" + id);
        setTimeout("location.reload()", "50")

    }

    function important(obj, id) {
        layer.confirm('Are you sure you want to put it in the important？', function (index) {
            //Send asynchronously delete data
            //We'll use async later, but we'll use async here
            $.get("/important?id=" + id);

            layer.msg('important!', {icon: 1, time: 1000});
            setTimeout("location.reload()", "500")
        });
    }


