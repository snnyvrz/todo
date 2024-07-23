interface item {
  done: boolean;
  id: string;
  title: string;
  due: string;
  modified: string;
}

type Data = item[];

const getData = async () => {
  const res = await fetch("http://localhost:8000/items");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return res.json();
};

export default async function Page() {
  const data: Data = await getData();

  return (
    <main className="p-4">
      <ul>
        {data.map((d, i) => (
          <li key={i}>{d.title}</li>
        ))}
      </ul>
    </main>
  );
}
