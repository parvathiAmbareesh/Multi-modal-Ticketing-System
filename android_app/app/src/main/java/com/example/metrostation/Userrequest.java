package com.example.metrostation;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.List;

public class Userrequest extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {
//    Spinner s1,s2;

    Button b1;
    ListView l1;
    EditText e1,e2;
    public static String fplace,tplace,amts;
    String attendance;
//    String[] station_id,value,station_name,date,stu_id;
    SharedPreferences sh;
    String tolatti,tolongi,folatti,folongi;
    String[] request_id,date,amount,fplaces,tplaces,value;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userrequest);


        sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
//        s2=(Spinner) findViewById(R.id.spinner1);
//        s1=(Spinner) findViewById(R.id.spinner2);
        l1=(ListView)findViewById(R.id.lv);
        l1.setOnItemClickListener(this);
        e2=(EditText) findViewById(R.id.e2);
        e1=(EditText) findViewById(R.id.e1);

        b1=(Button) findViewById(R.id.button);


//        s1.setOnItemSelectedListener(this);
//
//        s2.setOnItemSelectedListener(this);




        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Userrequest.this;
        String q = "/viewrequests?lid="+sh.getString("log_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);
//
//
//        JsonReq JR2 = new JsonReq();
//        JR2.json_response = (JsonResponse) Userrequest.this;
//        String q2 = "/viewspinnerfromplace";
//        q2 = q2.replace(" ", "%20");
//        JR2.execute(q2);



        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                fplace =e1.getText().toString();
                tplace=e2.getText().toString();

                GeocodingLocation locationAddress = new GeocodingLocation();
                locationAddress.getAddressFromLocation(tplace,
                        getApplicationContext(), new GeocoderHandler());

                locationAddress.getAddressFromLocation(fplace,
                        getApplicationContext(), new GeocoderHandler());



//                Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!"+sid, Toast.LENGTH_LONG).show();



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
                tolatti = tmp[0];
                tolongi = tmp[1];


//                folatti = tmp[0];
//                folongi = tmp[1];

                sendreq();
            } catch (Exception e) {
                Toast.makeText(getApplicationContext(), "check spelling" + e.toString(), Toast.LENGTH_LONG).show();
            }
        }
    }

    private void sendreq() {
        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Userrequest.this;
        String q = "/AddRequest?login_id=" + sh.getString("log_id", "")  +"&fplace=" +fplace+"&tplace="+tplace;
        q = q.replace(" ", "%20");
        JR.execute(q);
    }

    @Override
    public void response(JSONObject jo) {

        try {

            String method=jo.getString("method");
            if(method.equalsIgnoreCase("AddRequest")) {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "ADDED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    String rid=jo.getString("rid");

                    SharedPreferences.Editor e = sh.edit();
                    e.putString("rid", rid);
                    e.commit();

                    startActivity(new Intent(getApplicationContext(), Userviewrequest.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }
            }
            else if(method.equalsIgnoreCase("viewrequests"))
            {
                String status=jo.getString("status");
                Log.d("pearl",status);


                if(status.equalsIgnoreCase("success")){
                    JSONArray ja1=(JSONArray)jo.getJSONArray("data");

                    request_id=new String[ja1.length()];
                    date=new String[ja1.length()];
                    amount=new String[ja1.length()];
                    fplaces=new String[ja1.length()];
                    tplaces=new String[ja1.length()];
                    value=new String[ja1.length()];


                    for(int i = 0;i<ja1.length();i++)
                    {
                        request_id[i]=ja1.getJSONObject(i).getString("request_id");
                        date[i]=ja1.getJSONObject(i).getString("date");
                        amount[i]=ja1.getJSONObject(i).getString("amount");
                        fplaces[i]=ja1.getJSONObject(i).getString("fplace");
                        tplaces[i]=ja1.getJSONObject(i).getString("tplace");


                        value[i]="Date : "+date[i]+"\nAmount : "+amount[i]+"\nFrom Place : "+fplaces[i]+"\nto Places : "+tplaces[i];


                    }
                    ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),R.layout.custtext,value);
                    l1.setAdapter(ar);
                }
            }
//
//            else if(method.equalsIgnoreCase("viewspinnertoplace"))
//            {
//                String status=jo.getString("status");
//                Log.d("pearl",status);
//
//
//                if(status.equalsIgnoreCase("success")){
//                    JSONArray ja1=(JSONArray)jo.getJSONArray("data");
//
//                    station_id=new String[ja1.length()];
//
//                    station_name=new String[ja1.length()];
//                    value=new String[ja1.length()];
//
//
//                    for(int i = 0;i<ja1.length();i++)
//                    {
//                        station_id[i]=ja1.getJSONObject(i).getString("station_id");
//                        station_name[i]=ja1.getJSONObject(i).getString("station_name");
//
//
//                        value[i]=station_name[i];
//
//
//                    }
//                    ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),R.layout.custtext,value);
//                    s2.setAdapter(ar);
//                }
//            }


        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }

    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        String rid=request_id[i];
        amts=amount[i];
        SharedPreferences.Editor e = sh.edit();
        e.putString("rid", rid);
        e.commit();
        if(sh.getString("ttt","").equalsIgnoreCase("wp")) {
            SharedPreferences.Editor e1 = sh.edit();
            e1.putString("amts", amts);
            e1.commit();
            startActivity(new Intent(getApplicationContext(), AndroidBarcodeQrExample.class));
        }
        else if(sh.getString("ttt","").equalsIgnoreCase("wop")) {
            startActivity(new Intent(getApplicationContext(), Userviewrequest.class));
        }

    }

//
//    @Override
//    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
////        sid=station_id[i];
//
//        if (adapterView.getId()==R.id.spinner1)
//        {
//            sid=station_id[i];
//
//        }else if  (adapterView.getId()==R.id.spinner2){
//            sid1=station_id[i];
//        }
//    }
//
//    @Override
//    public void onNothingSelected(AdapterView<?> adapterView) {
//
//    }


}



