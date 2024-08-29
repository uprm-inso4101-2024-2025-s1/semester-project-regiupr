use telnet::Telnet;

fn main()
{
  let mut connection = Telnet::connect(("127.0.0.1", 23), 256)
          .expect("Couldn't connect to the server...");
  println!("Connected");
  loop 
  {
      let event = connection.read().expect("Read Error");
      println!("{:?}", event);
  }
}
