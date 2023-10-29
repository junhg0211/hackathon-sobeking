function drawGraph(type) {
    let weekData = {
        labels: [" ", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [
            {
                label: '', // 라벨을 비워 두거나 빈 문자열로 설정
                data: [0, 5000, 15000, 25000, 45000, 65000, 75000, 85000],
                borderColor: "rgba(106, 106, 164, 1)",
                borderWidth: 4,
                fill: false,
                lineTension: 0
            },
            {
                label: '', // 라벨을 비워 두거나 빈 문자열로 설정
                data: [0, 5000, 10000, 10000, 20000, 20000, 10000, 10000],
                borderColor: "rgba(189, 189, 189, 1)",
                borderWidth: 4,
                fill: false,
                lineTension: 0
            }
        ]
    };

    let monthData = {
        labels: [" ", "Week 1", "Week 2", "Week 3", "Week 4"],
        datasets: [
            {
                label: '', // 라벨을 비워 두거나 빈 문자열로 설정
                data: [0, 100000, 108000, 268000, 330000],
                borderColor: "rgba(106, 106, 164, 1)",
                borderWidth: 4,
                fill: false,
                lineTension: 0
            },
            {
                label: '', // 라벨을 비워 두거나 빈 문자열로 설정
                data: [0, 100000, 8000, 160000, 62000],
                borderColor: "rgba(189, 189, 189, 1)",
                borderWidth: 4,
                fill: false,
                lineTension: 0
            }
        ]
    };

    let data = type === 'week' ? weekData : monthData;

    new Chart(document.getElementById("consumptions-canvas"), {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: false,
                        labelString: '일자'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: false,
                        labelString: '가격'
                    }
                }]
            },
            legend: {
                display: false, // 범례를 비활성화
            }
        }
    });
}
let mode = 'week';
drawGraph(mode);

// -- event hander
let select = document.querySelector("#consumptions-select");
let title = document.querySelector(".consumptions-title");

select.addEventListener('change', e => {
    mode = e.target.value;

    drawGraph(mode);
    if (mode === 'week') {
        title.innerText = '주간 지출';
    } else {
        title.innerText = '월간 지출';
    }
});

// -- 소비 패턴 분석 버튼 event handling
let analysisButton = document.querySelector(".consumptions-analyse");

analysisButton.addEventListener('click', () => {
    window.location.href = "/analytics/" + mode;
});
