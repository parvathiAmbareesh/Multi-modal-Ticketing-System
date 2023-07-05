package com.example.metrostation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userviewrequest extends AppCompatActivity implements JsonResponse {
    Spinner s1,s2;

    EditText e1,e2,ne1,ne2;
    TextView t1,t2,t3;
    String nfplace,ntplace;
    Button b1;
    ListView l1;
    RadioButton r1,r2,r3,r4,r5;
    public static String tolatti,tolongi,folatti,folongi;
    public static String sid,sid1,types;
    String attendance;
    String[] fplace,value,tplace,amount,type;
    SharedPreferences sh;

  String [] stations={"Ernakulam south","Town hall","Jln stadium","M.g. Road renakulam","Maharaja's College","Edapally","Kadavanthra","Kaloor","Cochin University","Palarivattom","petta" ,"pathadipalam"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userviewrequest);


        sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        l1 = (ListView) findViewById(R.id.lvview);

        t1=(TextView)findViewById(R.id.textView8);

        t3=(TextView) findViewById(R.id.e2);
        t2=(TextView) findViewById(R.id.e1);

        ne2=(EditText) findViewById(R.id.ne2);
        ne1=(EditText) findViewById(R.id.ne1);
        b1=(Button) findViewById(R.id.button);

        r1=(RadioButton) findViewById(R.id.r1);
        r2=(RadioButton) findViewById(R.id.r2);
        r3=(RadioButton) findViewById(R.id.r3);
        r4=(RadioButton) findViewById(R.id.r4);
        r5=(RadioButton) findViewById(R.id.r5);

        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Userviewrequest.this;
        String q = "/Userviewrequestssss?rid="+sh.getString("rid","");
        q = q.replace(" ", "%20");
        JR.execute(q);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nfplace =ne1.getText().toString();
                ntplace=ne2.getText().toString();

                if(r1.isChecked())
                {
                    types="Metro";
                }
                else if(r2.isChecked())
                {
                    types="Water";
                }
                else if(r3.isChecked())
                {
                    types="Bus";
                }
                else if(r4.isChecked())
                {
                    types="Car";
                }
                else if(r5.isChecked())
                {
                    types="Auto";
                }


//                if  (stations.equals(nfplace)){
//                    if (stations.equals(ntplace)){


                        GeocodingLocation locationAddress = new GeocodingLocation();
                        locationAddress.getAddressFromLocation(nfplace,
                                getApplicationContext(), new GeocoderHandler());

                        locationAddress.getAddressFromLocation(ntplace,
                                getApplicationContext(), new GeocoderHandler1());

                        Toast.makeText(getApplicationContext(), tolatti+" "+tolongi+" "+folatti+" "+folongi, Toast.LENGTH_LONG).show();
                        JsonReq JR = new JsonReq();
                        JR.json_response = (JsonResponse) Userviewrequest.this;
                        String q = "/AddRequestss?rid=" + sh.getString("rid", "")  +"&fplace=" +nfplace+"&tplace="+ntplace+"&types="+types+"&fromlati="+folatti +"&fromlongi="+folongi +"&tolati="+tolatti+"&tolongi="+tolongi;
                        q = q.replace(" ", "%20");
                        JR.execute(q);
//                    }
//                }



            }
        });
    }

    class GeocoderHandler extends Handler {
        @Override
        public void handleMessage(Message message) {
            try {
                String locationAddress;
                switch (message.what) {
                    case 1:
                        Bundle bundle = message.getData();
                        locationAddress = bundle.getString("address");
                        break;
                    default:
                        locationAddress = null;
                }
                String[] tmp = locationAddress.split("\\,");
                Toast.makeText(getApplicationContext(), "check spelling" + tmp, Toast.LENGTH_LONG).show();
                folatti = tmp[0];
                folongi = tmp[1];


//                folatti = tmp[0];
//                folongi = tmp[1];

//                sendreq();
            } catch (Exception e) {
                Toast.makeText(getApplicationContext(), "check spelling" + e.toString(), Toast.LENGTH_LONG).show();
            }
        }
    }
        class GeocoderHandler1 extends Handler {
            @Override
            public void handleMessage(Message message) {
                try {
                    String locationAddress;
                    switch (message.what) {
                        case 1:
                            Bundle bundle = message.getData();
                            locationAddress = bundle.getString("address");
                            break;
                        default:
                            locationAddress = null;
                    }
                    String[] tmp = locationAddress.split("\\,");
                    Toast.makeText(getApplicationContext(), "check spelling" + tmp, Toast.LENGTH_LONG).show();
                    tolatti = tmp[0];
                    tolongi = tmp[1];


//                folatti = tmp[0];
//                folongi = tmp[1];

//                    sendreq();
                } catch (Exception e) {
                    Toast.makeText(getApplicationContext(), "check spelling" + e.toString(), Toast.LENGTH_LONG).show();
                }
            }
        }

//        private void sendreq() {
//            JsonReq JR = new JsonReq();
//            JR.json_response = (JsonResponse) Userviewrequest.this;
//            String q = "/AddRequestss?rid=" + sh.getString("rid", "")  +"&fplace=" +nfplace+"&tplace="+ntplace+"&types="+types;
//            q = q.replace(" ", "%20");
//            JR.execute(q);
//
//        }
//    }

    @Override
    public void response(JSONObject jo) {
        try {

            String method=jo.getString("method");
            if(method.equalsIgnoreCase("Userviewrequestssss")) {
                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {

                    t2.setText("From Place: "+jo.getString("fplace"));
                    t3.setText("To Place : "+jo.getString("tplace"));
                    t1.setText("Amount : "+jo.getString("total"));

                    JSONArray ja1 = (JSONArray) jo.getJSONArray("data1");

                    fplace = new String[ja1.length()];
                    tplace = new String[ja1.length()];
                    amount = new String[ja1.length()];
                    type = new String[ja1.length()];
                    value = new String[ja1.length()];

                    for (int i = 0; i < ja1.length(); i++) {


                        fplace[i] = ja1.getJSONObject(i).getString("fplaces");
                        tplace[i] = ja1.getJSONObject(i).getString("tplaces");
                        amount[i] = ja1.getJSONObject(i).getString("amounts");
                        type[i] = ja1.getJSONObject(i).getString("types");


                        value[i] = "From Place: " + fplace[i] + "\nTo Place: " + tplace[i] + "\nType: " + type[i] + "\nAmount: " + amount[i];

                    }
                    ArrayAdapter<String> ar = new ArrayAdapter<String>(getApplicationContext(), android.R.layout.simple_list_item_1, value);
                    l1.setAdapter(ar);
                }
            }
            else if(method.equalsIgnoreCase("AddRequestss")) {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "ADDED SUCCESSFULLY", Toast.LENGTH_LONG).show();
//                    String rid=jo.getString("rid");



                    startActivity(new Intent(getApplicationContext(), Userviewrequest.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }
            }

        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }

    public void onBackPressed()
    {
        // TODO Auto-generated method stub
        super.onBackPressed();
        Intent b=new Intent(getApplicationContext(),Userhome.class);
        startActivity(b);
    }
}