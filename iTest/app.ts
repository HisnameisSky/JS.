// 型定義：Pythonから送られてくるデータの構造を厳格に縛る（バグの排除）
interface Point {
    x: number;
    y: number;
}

interface WaveResponse {
    points: Point[];
}

class CanvasRepresentation {
    private canvas: HTMLCanvasElement;
    private ctx: CanvasRenderingContext2D;

    constructor(canvasId: string) {
        this.canvas = document.getElementById(canvasId) as HTMLCanvasElement;
        this.ctx = this.canvas.getContext('2d')!;
        this.startRenderLoop();
    }

    // 毎秒60回、Pythonの「意志」を「表象」に翻訳し続けるループ
    private async startRenderLoop(): Promise<void> {
        const render = async () => {
            try {
                // 1. Python（意志の源泉）からデータを取得
                const response = await fetch('http://localhost:8000/api/wave');
                const data: WaveResponse = await response.json();

                // 2. 画面をクリア（過去の残像を消去）
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

                // 3. 描画（表象の具現化）
                this.drawWave(data.points);

            } catch (error) {
                console.error("意志との通信が途絶えました:", error);
            }

            // 次のフレームを要求
            requestAnimationFrame(render);
        };

        render();
    }

    // 点の配列を、美しい一本の曲線（イラスト）として描き出す
    private drawWave(points: Point[]): void {
        if (points.length === 0) return;

        this.ctx.beginPath();
        this.ctx.moveTo(points[0].x, points[0].y);

        for (let i = 1; i < points.length; i++) {
            this.ctx.lineTo(points[i].x, points[i].y);
        }

        // 線のスタイリング（あなた好みの色に変える聖域）
        this.ctx.strokeStyle = '#3b82f6'; // 美しい青
        this.ctx.lineWidth = 4;
        this.ctx.lineCap = 'round';
        this.ctx.lineJoin = 'round';
        this.ctx.stroke();
    }
}

// 画面読み込み時にシステムを起動
window.addEventListener('DOMContentLoaded', () => {
    new CanvasRepresentation('myCanvas');
});
