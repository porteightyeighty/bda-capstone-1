from library import download_video, read_video_urls
import time
import multiprocessing as mp 


if __name__ == "__main__":
    urls = read_video_urls("data/video_urls.csv")
    # total_start = time.perf_counter()
    # for url in urls:
    #     start = time.perf_counter()
    #     download_video(url)
    #     end = time.perf_counter()
    #     elapsed = end - start
    #     serial_time = round(elapsed, 2)
    #     print(f"Download Time: {serial_time}")
    # total_end = time.perf_counter()
    # total_elapsed = total_end - total_start
    # total_serial_time = round(total_elapsed, 2)
    # with open('reports/sequential_report.md', 'a', encoding='utf-8') as f:
    #     f.write(str(total_serial_time))
    # print(f"Sequential Execution: {total_serial_time}")
    with mp.Pool() as pool:
        total_parallel_start = time.perf_counter()
        results = pool.map(download_video, urls)
        total_parallel_end = time.perf_counter()
        total_parallel_elapsed = total_parallel_end - total_parallel_start
        total_parallel_time = round(total_parallel_elapsed, 2)
        print(f"Parallel Execution: {total_parallel_time}")

